import sys
import traceback
from xml.dom import minidom   #for xml parsing


#g_players={'id':[]}
#g_ships={'id':[pos_x,pos_y,owner]}
#g_ports={'id':[pos_x,pos_y,owner]}

DEFAULT_CONTENT={'G':0, 'W':0, 'F':0, 'M':0, 'm':0, 'g':0, 'f':0, 'p':0, 'c':0, 'a':0 }
#(G)gold
#(W)wood
#(F)food
#(M)metal
#---------------
#(m)moussaillons
#(g)gunners
#(f)filibuster
#(p)pirate
#(c)cannon
#(a)ammo

g_players={}
g_ships={}
g_ports={}
g_ports_public={}

I_PORTS_POSX=0
I_PORTS_POSY=1
I_PORTS_OWNER=2
I_PORTS_GOLD_REMAINING=3
I_PORTS_PRODUCTION=4
I_PORTS_OP_IN_PROG=5
I_PORTS_CONTENT=6

I_SHIPS_POSX=0
I_SHIPS_POSY=1
I_SHIPS_OWNER=2
I_SHIPS_TYPE=3
I_PORTS_CONTENT=4

def convertStrToContent(string):
   last_index=0
   content=DEFAULT_CONTENT
   
   for index, char in enumerate(string):
      if char.isalpha():
         content[char]=string[last_index:index]
         last_index=index+1
   
   return content

def convertContentToStr(content):
   s=""
   
   for key in content:
      s+=str(content[key])+str(key)
   
   return s

###############################################################################
###############################################################################
###############################################################################

def player_clear():
   g_players={}

def player_new(id):
   g_players[id]=[]

def getAllPlayers():
   return g_players

###############################################################################
#galleon
#caravel
#gunboat
I_SHIPS_POSX=0
I_SHIPS_POSY=1
I_SHIPS_OWNER=2
I_SHIPS_TYPE=3
I_SHIPS_CONTENT=4
I_SHIPS_LEN=5

def port_clear():
   g_ships={}

def ship_new(id, pos_x, pos_y, id_owner, ship_type, content):
   g_ships[id]= ['']*I_SHIPS_LEN
   
   g_ships[id][I_SHIPS_POSX]=int(pos_x)
   g_ships[id][I_SHIPS_POSY]=int(pos_y)
   g_ships[id][I_SHIPS_OWNER]=id_owner
   g_ships[id][I_SHIPS_TYPE]=ship_type
   g_ships[id][I_SHIPS_CONTENT]=convertStrToContent(content)

def ship_set_pos(id, pos_x, pos_y):
   g_ships[id][I_SHIPS_POSX]=pos_x
   g_ships[id][I_SHIPS_POSY]=pos_y

def ship_set_owner(id, id_owner):
   g_ships[id][I_SHIPS_OWNER]=id_owner
   
def getPosition(id):
   return g_ships[id][I_SHIPS_POSX],g_ships[id][I_SHIPS_POSY]

#getState()

def getOwner(id):
   return g_ships[id][I_SHIPS_OWNER]
   
#gotoPort(port_id)
#estimateTimeToGo(pos)
#gotoPosition(pos)
#?attackShip(ship_id)
#approachShip(ship_id)
#askForSurrender()
#attack()
#moveInPort(unit_type, nb, port_id)
###############################################################################
I_PORTS_POSX=0
I_PORTS_POSY=1
I_PORTS_OWNER=2
I_PORTS_GOLD_REMAINING=3
I_PORTS_PRODUCTION=4
I_PORTS_OP_IN_PROG=5
I_PORTS_CONTENT=6
I_PORTS_LEN=7

I_PORTS_PUB_POSX=0
I_PORTS_PUB_POSY=1
I_PORTS_PUB_OWNER=2
I_PORTS_PUB_LEN=3


def port_clear():
   g_ports={}
   g_ports_public={}
   
def port_new(id, pos_x, pos_y, id_owner, gold_remaining, production, op_in_prog, content):
   g_ports[id]= ['']*I_PORTS_LEN
   
   g_ports[id][I_PORTS_POSX]=int(pos_x)
   g_ports[id][I_PORTS_POSY]=int(pos_y)
   g_ports[id][I_PORTS_OWNER]=id_owner
   g_ports[id][I_PORTS_GOLD_REMAINING]=int(gold_remaining)
   g_ports[id][I_PORTS_PRODUCTION]=convertStrToContent(production)
   g_ports[id][I_PORTS_OP_IN_PROG]=op_in_prog
   g_ports[id][I_PORTS_CONTENT]=convertStrToContent(content)
   
   
   g_ports_public[id]= ['']*I_PORTS_PUB_LEN
   
   g_ports_public[id][I_PORTS_PUB_POSX]=int(pos_x)
   g_ports_public[id][I_PORTS_PUB_POSY]=int(pos_y)
   g_ports_public[id][I_PORTS_PUB_OWNER]=id_owner
   
def port_set_owner(id, id_owner):
   g_ports[id][I_PORTS_OWNER]=id_owner
  
def getAllPort():
   return g_ports_public
   
def getWarehouseStocks(id):
   return g_ports[id][I_PORTS_CONTENT]
   
def getPortProduction(id):
   return g_ports[id][I_PORTS_PRODUCTION]

#getState()

def getOwner(id):
   return g_ports[id][I_PORTS_OWNER]

#generateUnit(unit_type, nb) #cancel also
#moveInShip(unit_type, nb, ship_id)
#setInTrade(unit_type, nb, price) #return trade_id
#cancelTrade(trade_id)
#askForSurrender()
#attack()
###############################################################################
###############################################################################
###############################################################################





###############################################################################
def init():

   player_clear()
   port_clear()
   ship_clear()
   
   print("Parsing xml input file...")
   
   try :
      xml = minidom.parse("world.xml")
   except:
    print("ERROR: Could not parse xml file")
    print(traceback.format_exc())
    sys.exit(1)
   
   for node in xml.getElementsByTagName("player") :
      id=node.getAttribute("id")
      player_new(id)
   
   for node in xml.getElementsByTagName("port") :
      id             = node.getAttribute("id")
      pos_x          = node.getAttribute("pos_x")
      pos_y          = node.getAttribute("pos_y")
      owner          = node.getAttribute("owner")
      gold_remaining = node.getAttribute("gold_remaining")
      production     = node.getAttribute("production")
      op_in_progress = node.getAttribute("op_in_progress")
      content        = node.getAttribute("content")
      port_new(id, pos_x, pos_y, owner, gold_remaining, production, op_in_progress, content)
   
   for node in xml.getElementsByTagName("ship") :
      id        = node.getAttribute("id")
      pos_x     = node.getAttribute("pos_x")
      pos_y     = node.getAttribute("pos_y")
      owner     = node.getAttribute("owner")
      ship_type = node.getAttribute("type")
      content   = node.getAttribute("content")
      ship_new(id, pos_x, pos_y, owner, ship_type, content)
   
   print("--- players ---")
   print(g_players)
   print("--- ships ---")
   print(g_ships)
   print("--- ports ---")
   print(g_ports)
   
   
   
init()





#getAllMyShips()
#getAllVisibleShips()
#getMapType(pos)

#port:
#getState()
#generateUnit(unit_type, nb) #cancel also
#moveInShip(unit_type, nb, ship_id)
#setInTrade(unit_type, nb, price) #return trade_id
#cancelTrade(trade_id)
#askForSurrender()
#attack()

#ship:
#getState()
#gotoPort(port_id)
#estimateTimeToGo(pos)
#gotoPosition(pos)
#?attackShip(ship_id)
#approachShip(ship_id)
#askForSurrender()
#attack()
#moveInPort(unit_type, nb, port_id)

#player:
#getStats()




























