from .psub_functions.demand import p_demand, s_demand, s_netflow
from .psub_functions.reward_rate import p_reward_rate, s_reward_rate
from .psub_functions.amm_k import s_amm_k
from .mechanism.supply import s_supply
from .mechanism.treasury import s_treasury_stables,s_liq_backing,s_reserves_in
from .policy.treasury import p_reserves_in
from .mechanism.rbs_price import s_ma_target,s_lb_target,s_price_history,s_price_target,s_lower_target_wall,s_upper_target_wall
from .policy.rbs_price import p_price_target

# OVERALL TODO: check if all the order are right

psub_blocks = [
    # update variables that depend on other variables

    # update_treasury_stables
    { # Warning: this part is actually "treasury_stables from yesterday" 
        "policies":{},
        "variables":{
            "treasury_stables":s_treasury_stables
        }
    },

    { # Warning: this part is actually "treasury_stables from yesterday" 
        "policies":{},
        "variables":{
            "liq_backing":s_liq_backing
        }
    },

    # update_price_history
    {
        "policies":{},
        "variables":{
            "price_history":s_price_history
        }
    },
    # ------------------RBS PRICE (based on what happened yesterday)--------------------
    #update two price targets
    {
        'policies':{},
        'variables':{
            'ma_target':s_ma_target,
            'lb_target':s_lb_target,
        }
    },
    #update actual price target today
    {
        'policies':{
            'price_target':p_price_target
            },
        'variables':{
            'price_target':s_price_target,
        }
    },
    # now update the walls around the target
    {
        'policies':{},
        'variables':{
            'lower_target_wall':s_lower_target_wall,
            'upper_target_wall':s_upper_target_wall
        }
    },


    # update supply expansion based on the activities happened from yesterday, plus providing rewards
    # update_supply
    { 
        'policies':{

        },
        'variables':{
            'supply':s_supply
        }
    },
    # update_reserves_in
    {
        'policies':{
        "reserves_in":p_reserves_in
        },
        'variables':{
            'reserves_in':s_reserves_in
        }
    },

    # update_AMM_k_block
    { 
        'policies':{},
        'variables':{
            'amm_k':s_amm_k,#Note: for now it's actually constant k
        }
    },


    
    # -----------------------------------------------------
]
demand_update_block = {
    'policies': {
        'supply_demand': p_demand
    },
    'variables': {
        'market_demand_supply': s_demand,
        'net_flow': s_netflow
    }
}