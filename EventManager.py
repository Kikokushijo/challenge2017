class BaseEvent(object):
    """
    A superclass for any events that might be generated by
    an object and sent to the EventManager.
    """
    def __init__(self):
        self.name = "Generic event"
    def __str__(self):
        return self.name

class Event_Initialize(BaseEvent):
    """
    Initialize event.
    """
    def __init__(self):
        self.name = "Initialize event"
    def __str__(self):
        return self.name

class Event_Restart(BaseEvent):
    def __init__(self):
        self.name = "Restart event"
    def __str__(self):
        return self.name

class Event_Quit(BaseEvent):
    """
    Quit event.
    """
    def __init__ (self):
        self.name = "Quit event"
    def __str__(self):
        return self.name

class Event_StateChange(BaseEvent):
    """
    change state event.
    """
    def __init__(self, state):
        self.name = "StateChange event"
        self.state = state
    def __str__(self):
        return "{0} => StateTo:{1}".format(self.name, self.state)

class Event_EveryTick(BaseEvent):
    """
    Tick event.
    """
    def __init__ (self):
        self.name = "Tick event"
    def __str__(self):
        return self.name

class Event_EverySec(BaseEvent):
    """
    Sec event.
    """
    def __init__(self):
        self.name = "Sec event"
    def __str__(self):
        return self.name

class Event_TimeUp(BaseEvent):
    """
    TimeUp event.
    """
    def __init__(self):
        self.name = "TimeUp event"
    def __str__(self):
        return self.name

class Event_Move(BaseEvent):
    """
    Move event.
    """
    def __init__(self, player, direction):
        self.name = "Move event"
        self.PlayerIndex = player
        self.Direction = direction
    def __str__(self):
        return "{0} => Playerindex={1}, DirectionTo:{2}".format(self.name, self.PlayerIndex, self.Direction)

class Event_PlayerModeChange(BaseEvent):
    """
    Mode change event.
    """
    def __init__(self, player):
        self.name = "ModeChange event"
        self.PlayerIndex = player
    def __str__(self):
        return "{0} => Playerindex={1}".format(self.name, self.PlayerIndex)

class Event_SkillCard(BaseEvent):
    """
    SkillCard event.
    """
    def __init__(self,player,skill):
        self.name = "SkillCard event"
        self.PlayerIndex = player
        self.SkillIndex = skill
    def __str__(self):
        return "{0} => Playerindex={1}, SkillIndex={2}".format(self.name, self.PlayerIndex, self.SkillIndex)

class Event_Action(BaseEvent):
    """
    Action event.
    """
    def __init__(self, player, action):
        self.name = "Action event"
        self.PlayerIndex = player
        self.ActionIndex = action
    def __str__(self):
        return "{0} => Playerindex={1}, ActionIndex={2}".format(self.name, self.PlayerIndex, self.ActionIndex)

class EventManager(object):
    """
    We coordinate communication between the Model, View, and Controller.
    """
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        """ 
        Adds a listener to our spam list. 
        It will receive Post()ed events through it's notify(event) call. 
        """
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        """ 
        Remove a listener from our spam list.
        This is implemented but hardly used.
        Our weak ref spam list will auto remove any listeners who stop existing.
        """
        if listener in self.listeners.keys():
            del self.listeners[listener]
        
    def Post(self, event):
        """
        Post a new event to the message queue.
        It will be broadcast to all listeners.
        """
        # this segment use to debug
        if not (isinstance(event, Event_EveryTick) or isinstance(event, Event_EverySec)):
            print( str(event) )
        for listener in self.listeners.keys():
            listener.notify(event)
