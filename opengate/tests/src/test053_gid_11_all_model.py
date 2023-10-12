#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from test053_gid_helpers2 import *

if __name__ == "__main__":
    paths = get_default_test_paths(__file__, "", output_folder="test053")

    # bi213 83 213
    # ac225 89 225
    # fr221 87 221
    # pb 82 212
    # po 84 213
    # tl 81 209
    z = 89
    a = 225
    nuclide, _ = get_nuclide_and_direct_progeny(z, a)
    print(nuclide)
    sim_name = f"{nuclide.nuclide}_11_model"

    sim = gate.Simulation()
    create_sim_test053(sim, sim_name)

    # sources
    activity_in_Bq = 500
    s = add_source_model(sim, z, a, activity_in_Bq)
    s.atomic_relaxation_flag = True
    s.isomeric_transition_flag = True

    # go
    sec = g4_units.second
    min = g4_units.minute
    start_time = 15 * min
    end_time = start_time + 2 * min
    duration = end_time - start_time
    print(f"start time {start_time / sec}")
    print(f"end time {end_time / sec}")
    print(f"Duration {duration / sec}")
    print(f"Ions {activity_in_Bq * duration / sec:.0f}")
    sim.run_timing_intervals = [[start_time, end_time]]

    # go
    output = sim.start(True)

    # print stats
    stats = output.get_actor("stats")
    print(stats)

    # compare
    warning(f"check root files")
    root_ref = paths.output_ref / f"test053_{nuclide.nuclide}_10_ref.root"
    # root_ref = paths.output / f"test053_Ac-225_10_TEST.root"
    root_model = sim.get_actor_user_info("phsp").output
    is_ok = compare_root_energy(
        root_ref,
        root_model,
        start_time,
        end_time,
        model_index=-1,
        tol=0.035,
        range=[0, 500],
    )

    test_ok(is_ok)
