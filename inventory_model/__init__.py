from gym.envs.registration import register

register(
    id='inventory_model-v0',
    entry_point='inventory_model.envs:Inventory',
)

register(
    id='inventory_cont_model-v0',
    entry_point='inventory_model.envs:ContInventory',
)

register(
    id='inventory_cont_config_model-v0',
    entry_point='inventory_model.envs:ContInventoryConfig',
)

register(
    id='inventory_cont_config_validation_model-v0',
    entry_point='inventory_model.envs:ContInventoryConfigValidation',
)

register(
    id='inventory_cont_config_fix_model-v0',
    entry_point='inventory_model.envs:ContInventoryConfigFix',
)