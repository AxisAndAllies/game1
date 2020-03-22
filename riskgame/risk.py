from dataclasses import dataclass

class RiskState:
    """Stores territories, armies, and connections
    """
    def __init__():
        pass


class RiskGame:
    """Risk Game emulator
    
    The game can be joined by multiple agents. At this point, is waiting for players.

    After start() is called:
    - players are fixed
    - every player gets a turn
    """
    
    def __init__(self, agents = None):

        self.state = None

        self.agents = dict()
        if agents:
            for i in agents:
                self.join(i)

    def on_agent_leave(self, agent):
        if agent.id in self.agents:
            del self.agents[agent.id]
        printf(f'{agent.id} leaving game...')
        
    def on_agent_join(self, agent):
        print(f'{agent.id} joining game...')
        self.agents[agent.id] = agent
    
    def start(self):
        self.state = RiskState()
        
        # Store a list of agent ids, for turn order
        self.agent_ids = list(self.agents.keys())
        self.current_agent_index = 0

        self.current_agent_id = self.agent_ids[self.current_agent_index]

    def resolve(self, action):
        """In Risk, you can do multiple things in your turn. Resolves a single step

        A turn has multiple components

        Receive armies
        - In this phase, you receive reinforcements.
        - You can trade in cards to get more reinforcements
        - A RECEIVE_ARMIES action consists of:
            - (nothing, since we're not dealing with cards)
            = Returns: [# reinforcements] you get
        
        Reinforce
        - In this phase, you place your reinforcements!
        - A REINFORCE action is:
            - an nd.array whose length is equal to the territories and whose sum is [# reinforcements]
            = Returns: (nothing)

        Attack
        - In this phase, you can decide to attack a territory
        - An ATTACK action consists of:
            - [from_territory, to_territory] - integers corresponding to the territory to attack
            - [units] - # of units to send
            = Returns: (nothing)
        
        Attack - Battle
        - Once you decide to attack, you are now in a battle
        - A BATTLE action consists of:
            - [num_dice] - how many die to roll
            = Returns: units left over?
        - An END_BATTLE action will allow you to attack again

        Attack - Win
        - If you win the attack, you can issue a CAPTURE command
            - [num_units] - # units to send over
        - You can attack again
        
        Game details:
        If you've captured at least 1 territory, you can get a RiskCard
        If you eliminate your opponents, you get all their RiskCards
        It's possible that this forces you to Receive reinforcements again

        Fortify
        - In this phase, you can move your armies around the graph
        - A FORTIFY action consists of:
            - [(from_territory, to_territory, units)] - a list of these moves, where from_territory and to_territory have to be connected
        """
        print('Not implemented', action)
    
    def step(self, action):

        # only the current player can make an action
        if action['agent_id'] != self.current_agent_id:
            print('Nope')
            return

        # resolve the action
        self.resolve(action)
        
        # get the next player
        num_players = len(self.agent_ids)
        self.current_agent_index = (self.current_agent_index + 1) % num_players
        self.current_agent_id = self.agent_ids[self.current_agent_index]

        observation = self.observation()

        return (observation, self.current_agent_id)

    def observation(self):
        return self.state
        
    def end(self):
        """Ends the game"""
        print(f'Game ending!')
        self.agents = dict()


# And here, we have our agent
class RiskAgent:
    """Game playing agent
    
    This is the interface for interacting with the RiskGame
    """
    def __init__(self, id):
        self.id = id
        self.game = None

    def step(self, action):
        
        return (obs, reward, final)

    def join(self, game):
        self.game = game
        self.game.on_agent_join(self)

    def leave(self):
        if self.game:
            self.game.on_agent_leave(self)
