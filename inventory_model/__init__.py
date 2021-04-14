from gym.envs.registration import register

register(
    id='inventory_model-v0',
    entry_point='inventory_model.envs:Inventory',
)

register(
    id='inventory_cont_model-v0',
    entry_point='inventory_model.envs:ContInventory',
)