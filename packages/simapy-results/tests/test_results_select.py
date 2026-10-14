"""``Container.select``: SIMA's signal requirements, matched as SIMA matches them.

The ``test_*`` functions named after a Java method transcribe that case of
sima-platform's ``SignalItemQueryTest``, on the same tree. SIMA's ``yunit`` is
``unit`` here. Where SIMA queries a list of top-level items, each is selected
from separately: like each item SIMA is given, the container ``select`` is
called on is itself a candidate.
"""

import pytest

from simapy_results import Container, open_results
from simapy_results._build import add_signal, graft, rename_duplicates
from simapy_results._node import constant

from .conftest import DATA

WAVE = "1st order wave force (koko)"
FORCES = ("XRforce", "YRforce", "ZRforce")
MOMENTS = ("Moment_XRaxis", "Moment_YRaxis", "Moment_ZRaxis")
DOFS = ("X", "Y", "Z")


def _signal(parent: Container, name: str, **attributes: str) -> None:
    add_signal(parent, constant(name, 0.0, xunit="s", **attributes))


def _wave_force(body: str) -> Container:
    wave = Container(WAVE, type="force", body=body)
    for name in FORCES:
        _signal(wave, name, body=body, unit="N")
    for name in MOMENTS:
        _signal(wave, name, body=body, unit="N*m")
    return wave


def _position(body: str) -> Container:
    position = Container("position", type="position", body=body)
    for dof in DOFS:
        _signal(position, dof, type="translation", body=body, unit="N")
    return position


def _body(name: str) -> Container:
    """``createBodyContainer``."""
    body = Container(name, body=name)
    graft(body, _position(name))
    graft(body, _wave_force(name))
    return body


def _task(name: str, *bodies: str) -> Container:
    task = Container(name, body=name)
    for body in bodies:
        graft(task, _body(body))
    return task


def _query(roots, *paths, **requirements) -> list[str]:
    """SIMA's query over several top-level items, keyed from each item's name."""
    return sorted(
        f"{root.name}/{key}" for root in roots for key in root.select(*paths, **requirements)
    )


def _under(body: str, container: str, names) -> list[str]:
    return [f"{body}/{container}/{name}" for name in names]


def _all(body: str) -> list[str]:
    return sorted(_under(body, "position", DOFS) + _under(body, WAVE, FORCES + MOMENTS))


# -- SignalItemQueryTest ---------------------------------------------------


def test_simple_container_no_requirements():
    """testSimpleContainerNoRequirements"""
    assert _query([_body("Body1")]) == _all("Body1")


def test_simple_signal_no_requirements():
    """testSimpleSignalNoRequirements"""
    holder = Container("b1")
    _signal(holder, "XRforce", body="b1", unit="N")

    assert list(holder.select()) == ["XRforce"]


@pytest.mark.parametrize("unit, found", [
    ("N", ["XRforce"]),
    ("N*m", []),
    (["N", "N*m"], ["XRforce"]),
], ids=["testSimpleSignalWithUnit", "testSimpleSignalWithWrongUnit",
        "testSimpleSignalWithSeveralUnits"])
def test_simple_signal_with_units(unit, found):
    holder = Container("b1")
    _signal(holder, "XRforce", body="b1", unit="N")

    assert list(holder.select(unit=unit)) == found


def test_simple_container_match_top_path():
    """testSimpleContainerMatchTopPath"""
    assert _query([_body("Body1")], "Body1") == _all("Body1")


def test_simple_container_does_not_match():
    """testSimpleContainerDoesNotMatchMatch"""
    assert _query([_body("Body1")], "Body2") == []


def test_position_query():
    """testPositionQuery"""
    second = _body("Body2")
    graft(second, _wave_force("Body2"))

    found = _query([_body("Body1"), second], body="Body2", type="position")

    assert found == _under("Body2", "position", DOFS)


def test_simple_container_match_deep_path():
    """testSimpleContainerMatchDeepPath"""
    task = _task("task1", "body1")

    found = task.select(f"task1.body1.{WAVE}.Moment_XRaxis")

    assert list(found) == [f"body1/{WAVE}/Moment_XRaxis"]


def test_items_in_container_path():
    """testItemsInContainerPath"""
    task = _task("task1", "body1")

    found = task.select(f"task1.body1.{WAVE}")

    assert list(found) == [f"body1/{WAVE}/{name}" for name in FORCES + MOMENTS]


def test_that_name_requirement_only_selects_that_item():
    """testThatNameRequirementOnlySelectsThatItem"""
    assert list(_body("body").select(name="XRforce")) == [f"{WAVE}/XRforce"]


@pytest.mark.parametrize("call", [
    lambda task: task.select(f"task1.body1.{WAVE}", unit=["N", "N*m"]),
    lambda task: task.select(unit=["N*m", "N"], path=f"task1.body1.{WAVE}"),
], ids=["testItemsInContainerPathWithTwoUnits",
        "testItemsInContainerPathWithTwoUnits_DifferentRequirementsOrder"])
def test_items_in_container_path_with_two_units(call):
    found = call(_task("task1", "body1"))

    assert sorted(found) == sorted(f"body1/{WAVE}/{name}" for name in FORCES + MOMENTS)


def test_items_in_different_parent_folder():
    """testItemsInDifferentParentFolder"""
    task = _task("task1", "body1", "body2")

    found = task.select(name=WAVE)

    assert sorted(found) == sorted(
        f"{body}/{WAVE}/{name}" for body in ("body1", "body2") for name in FORCES + MOMENTS
    )


def test_dof_query():
    """testDOFQuery"""
    assert _query([_body("Body1"), _body("Body2")], body="Body1") == _all("Body1")


def test_exact_container_query():
    """testExactContainerQuery"""
    assert _query([_body("Body1"), _body("Body11")], "Body1") == _all("Body1")


@pytest.mark.parametrize("body", ["Body*", "Body?"],
                         ids=["testSimpleWildcardInBody", "testQuestionMarkRequirementOnBody"])
def test_wildcards_on_body(body):
    found = _query([_body("Body1"), _body("Body2")], body=body)

    assert found == sorted(_all("Body1") + _all("Body2"))


def test_wildcard_in_body_with_other_requirements():
    """testWildcardInBodyWithOtherRequirements"""
    found = _query([_body("Body1"), _body("Body2")], body="Body*", type="translation")

    assert found == _under("Body1", "position", DOFS) + _under("Body2", "position", DOFS)


def test_question_mark_and_wildcard_requirement_on_name():
    """testQuestionMarkAndWildcardRequirementOnName"""
    found = _query([_body("Body1"), _body("Body2")], name="B?*?")

    assert found == sorted(_all("Body1") + _all("Body2"))


def test_double_path_query():
    """testDoublePathQuery"""
    found = _query([_body("Body1"), _body("Body2")], "Body1", "Body2")

    assert found == sorted(_all("Body1") + _all("Body2"))


def test_translation_query():
    """testTranslationQuery"""
    found = _query([_body("Body1"), _body("Body2")], type="translation")

    assert found == _under("Body1", "position", DOFS) + _under("Body2", "position", DOFS)


@pytest.mark.parametrize("call", [
    lambda roots: _query(roots, "Body1", unit="N"),
    lambda roots: _query(roots, unit="N", path="Body1"),
], ids=["testQueryWithPathAndUnit_InThatOrder / testQueryForForces_ShallNotGiveMoment",
        "testQueryWithUnitAndPath_InThatOrder"])
def test_query_with_path_and_unit(call):
    found = call([_body("Body1"), _body("Body2")])

    assert found == sorted(_under("Body1", "position", DOFS) + _under("Body1", WAVE, FORCES))


def test_query_for_moment_shall_not_give_force():
    """testQueryForMoment_ShallNotGiveForce"""
    found = _query([_body("Body1"), _body("Body2")], "Body1", unit="N*m")

    assert found == _under("Body1", WAVE, MOMENTS)


@pytest.mark.parametrize("unit", ["kg", "Q"], ids=[
    "testQueryWhichShallDeliverNoResult", "testQueryForPathAndNonExistingUnit",
])
def test_query_for_path_and_a_unit_nothing_has(unit):
    assert _query([_body("Body1"), _body("Body2")], "Body1", unit=unit) == []


@pytest.mark.parametrize("call", [
    lambda roots: _query(roots, f"Body1.{WAVE}.Moment_XRaxis", unit="N*m"),
    lambda roots: _query(roots, unit="N*m", path=f"Body1.{WAVE}.Moment_XRaxis"),
], ids=["testQueryWhithPathToDataItemAndUnit_InThatOrder",
        "testQueryWhithUnitAndPathToDataItem_InThatOrder"])
def test_query_with_path_to_a_signal_and_unit(call):
    assert call([_body("Body1"), _body("Body2")]) == [f"Body1/{WAVE}/Moment_XRaxis"]


def test_wildcard_return_everything():
    """testWildcard_ReturnEverything"""
    found = _query([_body("Body1"), _body("Body2")], "*")

    assert found == sorted(_all("Body1") + _all("Body2"))


def test_wildcard_return_all_position_items():
    """testWildcard_ReturnAllPositionItems"""
    found = _query([_body("Body1"), _body("Body2")], "*.position")

    assert found == _under("Body1", "position", DOFS) + _under("Body2", "position", DOFS)


def test_wildcard_return_wave_force_items_from_body1():
    """testWildcard_ReturnWaveForceItemsFromBody1"""
    found = _query([_body("Body1"), _body("Body2")], f"Body1.{WAVE}.*Rforce")

    assert found == _under("Body1", WAVE, FORCES)


def test_wildcard_return_all_wave_force_items():
    """testWildcard_ReturnAllWaveForceItems"""
    found = _query([_body("Body1"), _body("Body2")], f"Body*.{WAVE}.*Rforce")

    assert found == _under("Body1", WAVE, FORCES) + _under("Body2", WAVE, FORCES)


def _simple_bodies() -> list[Container]:
    bodies = []
    for name in ("Body1", "Body12"):
        body = Container(name, body=name)
        _signal(body, "X", type="translation", body=name, unit="N")
        bodies.append(body)
    return bodies


def test_return_only_matches_from_given_container():
    """testReturnOnlyMatchesFromGivenContainer"""
    assert _query(_simple_bodies(), "Body1") == ["Body1/X"]


def test_wildcard_return_only_matches_from_given_container():
    """testWildcard_ReturnOnlyMatchesFromGivenContainer"""
    assert _query(_simple_bodies(), "*Body1") == ["Body1/X"]


def test_filter_on_names_and_body_returns_all_names_for_the_given_body():
    """testFilterOnNamesAndBody_ReturnsAllNamesForTheGivenBody"""
    task = Container("task")
    condition = graft(task, Container("condition"))
    for name in ("TROLLC", "S7000"):
        body = graft(condition, Container(name, body=name))
        position = graft(body, Container("Global pos. (time domain)"))
        for signal in ("XLvelocityTotalmotion", "XGtranslationTotalmotion"):
            _signal(position, signal, body=name)
    names = ["XLvelocityTotalmotion", "XGtranslationTotalmotion"]
    expected = [
        "condition/S7000/Global pos. (time domain)/XLvelocityTotalmotion",
        "condition/S7000/Global pos. (time domain)/XGtranslationTotalmotion",
    ]

    assert list(task.select(body="S7000", name=names)) == expected
    assert list(task.select(name=names, body="S7000")) == expected


def test_selected_subtree_is_structurally_equivalent():
    """selectedSubtreeIsStructurallyEquivalent: a same-named container at another
    depth does not match."""
    c1 = Container("c1")
    c3 = graft(graft(c1, Container("c2")), Container("c3"))
    add_signal(c3, constant("i1", 1))
    elsewhere = Container("c3")
    add_signal(elsewhere, constant("i2", 2))

    assert _query([c1, elsewhere], "c1.c2.c3") == ["c1/c2/c3/i1"]


# -- the matcher -----------------------------------------------------------


def _named(*names: str) -> Container:
    holder = Container("root")
    for name in names:
        _signal(holder, name)
    return holder


def test_a_dot_is_literal():
    assert list(_named("X.Y", "XzY").select(name="X.Y")) == ["X.Y"]


def test_parentheses_are_literal():
    holder = _named("force (koko)", "force koko")

    assert list(holder.select(name="force (koko)")) == ["force (koko)"]
    assert list(holder.select(name="force (*)")) == ["force (koko)"]


def test_a_question_mark_is_zero_or_one_character():
    assert list(_named("X", "XY", "XYZ").select(name="X?")) == ["X", "XY"]


def test_without_a_wildcard_only_equality_matches():
    holder = _named("XRforce", "XRforces", "aXRforce")

    assert list(holder.select(name="XRforce")) == ["XRforce"]
    assert list(holder.select(name="XRforc")) == []


@pytest.mark.parametrize("requirement, found", [
    ("*force", list(FORCES)),
    ("Moment*", list(MOMENTS)),
    ("Moment*axis", list(MOMENTS)),
    ("*Rforce*", list(FORCES)),
    ("*_XR*", ["Moment_XRaxis"]),
    ("*R*s", list(MOMENTS)),
    ("X*R*e", ["XRforce"]),
    ("Moment_*R*s", list(MOMENTS)),
])
def test_one_and_two_star_forms(requirement, found):
    """The forms SIMA's Matcher short-cuts with string tests."""
    assert [key.rsplit("/", 1)[1] for key in _body("Body1").select(name=requirement)] == found


def test_other_characters_are_regex_once_a_wildcard_is_present():
    found = _body("Body1").select(name="[XY]Rforce?")

    assert [key.rsplit("/", 1)[1] for key in found] == ["XRforce", "YRforce"]


def test_other_characters_are_literal_with_at_most_two_stars():
    """Matcher compares literally unless ``.?()`` or a third ``*`` appears."""
    assert list(_named("X", "XX", "X+").select(name="X+*")) == ["X+"]
    assert list(_named("XRforce", "[XY]Rforce").select(name="[XY]R*")) == ["[XY]Rforce"]


def test_the_container_called_on_is_a_candidate_too():
    body = _body("Body1")

    assert sorted(body.select(name="Body1")) == sorted(
        key.split("/", 1)[1] for key in _all("Body1"))
    assert sorted(body.select("*Body1")) == sorted(body.select())


def test_an_invalid_pattern_says_which_requirement():
    with pytest.raises(ValueError, match="invalid requirement"):
        _body("Body1").select(name="X[?")


def test_a_star_crosses_levels():
    assert _query([_body("Body1")], "Body1*X") == ["Body1/position/X"]


def test_a_path_without_a_star_and_without_an_exact_hit_selects_nothing():
    assert _query([_body("Body1")], "Body1.positio") == []
    assert _query([_body("Body1")], "Body1.position.X.deeper") == []


# -- how requirements combine ----------------------------------------------


def test_values_of_one_key_are_alternatives():
    found = _body("Body1").select(name=("X", "XRforce"))

    assert list(found) == ["position/X", f"{WAVE}/XRforce"]


def test_different_keys_must_all_hold():
    body = _body("Body1")

    assert list(body.select(name="X", unit="N")) == ["position/X"]
    assert list(body.select(name="X", unit="N*m")) == []


def test_a_matching_container_brings_its_whole_subtree():
    """The wave force signals carry no type; their container does."""
    found = _body("Body1").select(type="force")

    assert list(found) == [f"{WAVE}/{name}" for name in FORCES + MOMENTS]


def test_naming_an_ancestor_exactly_selects_everything_below_it():
    position = _task("task1", "body1").container("body1/position")

    assert list(position.select("task1.body1")) == list(DOFS)


def test_no_requirement_selects_every_signal():
    task = _task("task1", "body1", "body2")

    assert sorted(task.select()) == sorted(
        f"{body}/{key.split('/', 1)[1]}" for body in ("body1", "body2") for key in _all(body)
    )


# -- keys -------------------------------------------------------------------


def test_keys_are_relative_and_go_straight_back_into_getitem():
    task = _task("task1", "body1")
    body = task.container("body1")

    assert list(body.select("task1.body1.position.X")) == ["position/X"]
    for key, signal in body.select().items():
        assert body[key] is signal


def test_same_named_siblings_are_selected_under_their_own_keys():
    root = Container("root")
    first = graft(root, Container("x"))
    second = graft(root, Container("x"))
    _signal(first, "s")
    _signal(second, "s")
    rename_duplicates([root])

    assert list(root.select()) == ["x/s", "x_duplicate_1/s"]
    assert list(root.select("root.x_duplicate_1.s")) == ["x_duplicate_1/s"]
    assert root.select("root.x")["x/s"] is first.signal("s")


# -- the real fixture -------------------------------------------------------


RUN = DATA / "Simple_Flexible_Riser" / "Initial"


def test_selection_on_a_real_run():
    res = open_results(RUN)

    assert list(res.select("*.F-MAX")) == [
        "Initial/Dynamic/RiserLine/Force envelope curve/F-MAX"
    ]
    assert list(res.select(
        "Simple_Flexible_Riser.Initial.Static.RiserLine.Static forces.EFF. TENSION"
    )) == ["Initial/Static/RiserLine/Static forces/EFF. TENSION"]
    assert sorted(res.select(name="EFF. TENSION")) == [
        "Initial/Dynamic/RiserLine/Force standard deviation/EFF. TENSION",
        "Initial/Static/RiserLine/Static forces/EFF. TENSION",
    ]


def test_a_type_requirement_on_a_real_run():
    res = open_results(RUN)

    lines = res.select(type="line")

    assert lines
    assert all(key.split("/")[2] == "RiserLine" for key in lines)
    assert len(lines) == sum(
        1 for key in res.select() if key.split("/")[2:3] == ["RiserLine"]
    )


def test_a_sub_container_matches_the_same_absolute_paths():
    run = open_results(RUN).run

    found = run.select("Simple_Flexible_Riser.Initial.Dynamic.*.F-MAX")

    assert list(found) == ["Dynamic/RiserLine/Force envelope curve/F-MAX"]
    assert run["Dynamic/RiserLine/Force envelope curve/F-MAX"] is found[
        "Dynamic/RiserLine/Force envelope curve/F-MAX"
    ]
