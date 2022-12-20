from ..policy.treasury_market_operations import real_bid_capacity_cushion_policy, real_ask_capacity_cushion_policy


def p_real_bid_capacity_cushion(_params, substep, state_history, state) -> dict:
    prev_day = state_history[-1][-1]
    bid_counter = state["bid_counter"]
    min_counter_reinstate = _params["min_counter_reinstate"]
    with_reinstate_window = _params["with_reinstate_window"]
    natural_price = state["natural_price"]
    lower_target_cushion = state["lower_target_cushion"]
    bid_capacity_target_cushion = state["bid_capacity_target_cushion"]
    bid_capacity_target_cushion_prior = prev_day["bid_capacity_target_cushion"]
    lower_target_wall = state["lower_target_wall"]
    net_flow = state["net_flow"]
    reserves_in = state["reserves_in"]
    liq_stables_prior = prev_day["liq_stables"]
    amm_k = state["amm_k"]
    bid_capacity_cushion_prior = prev_day["bid_capacity_cushion"]

    return {"bid_capacity_cushion": real_bid_capacity_cushion_policy(bid_counter, min_counter_reinstate, with_reinstate_window, natural_price, lower_target_cushion, bid_capacity_target_cushion, bid_capacity_target_cushion_prior, lower_target_wall, net_flow, reserves_in, liq_stables_prior, amm_k, bid_capacity_cushion_prior)}


def p_real_ask_capacity_cushion(_params, substep, state_history, state) -> dict:
    prev_day = state_history[-1][-1]

    ask_counter = state["ask_counter"]
    min_counter_reinstate = _params["min_counter_reinstate"]
    with_reinstate_window = _params["with_reinstate_window"]
    natural_price = state["natural_price"]
    upper_target_cushion = state["upper_target_cushion"]
    ask_capacity_target_cushion = state["ask_capacity_target_cushion"]
    upper_target_wall = state["upper_target_wall"]
    ask_capacity_cushion_prior = prev_day["ask_capacity_cushion"]
    net_flow = state["net_flow"]
    reserves_in = state["reserves_in"]
    liq_stables_prior = prev_day["liq_stables"]
    amm_k = state["amm_k"]

    return {"ask_capacity_cushion": real_ask_capacity_cushion_policy(ask_counter, min_counter_reinstate, with_reinstate_window, natural_price, upper_target_cushion, ask_capacity_target_cushion, upper_target_wall, ask_capacity_cushion_prior, net_flow, reserves_in, liq_stables_prior, amm_k)}


def s_bid_capacity_cushion(_params, substep, state_history, state, _input) -> tuple:
    return ("bid_capacity_cushion", _input["bid_capacity_cushion"])


def s_ask_capacity_cushion(_params, substep, state_history, state, _input) -> tuple:
    return ("ask_capacity_cushion", _input["ask_capacity_cushion"])