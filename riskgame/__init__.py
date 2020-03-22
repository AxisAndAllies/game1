from gym.envs.registration import register

register(
    id='risk-v0',
    entrypoint='riskgame.envs:RiskEnv'
)