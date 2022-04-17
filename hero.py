class hero:
  """Bantuan Library Hero:

  NAME
    hero
  
  DESCRIPTION
    Library untuk bermain MOBA sederhana untuk Python
    =================================================
    Library hero mendukung pembuatan hero dan
    memfasilitasi pertarungan hero.

    Sumber : https://drive.google.com/file/d/1jsHSA0UrShh6rXSp5zQtnvlv9kLwMo97/view?usp=sharing

  CLASSES
    fighter
    mage
  
  FUNCTION
    get_info_hero() -> tuple
    memberikan_serangan() -> float
    menerima_serangan(float)
    recall()
    ultimate() -> float
  """

  nama = ''
  hp = 0
  mana = 0
  attack = 0
  defense = 0
  max_hp = 0
  max_mana = 0
    
  def get_info_hero(self):
    return self.nama, self.hp, self.mana, self.attack, self.defense
  
  def memberikan_serangan(self):
    print(f'{self.nama} memberikan serangan sebesar {self.attack}')
    return self.attack
  
  def menerima_serangan(self, serangan):
    if serangan > self.defense:
      print(f'{self.nama} menerima serangan sebesar {serangan - self.defense}')
      self.hp = self.hp - (serangan - self.defense) # rumus menerima serangan
      print(f'sisa HP {self.nama} = {self.hp}')
    if self.hp <= 0:                              # jika HP habis, maka tumbang
      print(f'{self.nama} tumbang dan respawn')
      self.recall()
  
  def recall(self):
    print(f'sisa HP = {self.hp}, sisa Mana = {self.mana}')
    self.hp = self.max_hp
    self.mana = self.max_mana
    print(f'mengisi ulang HP {self.nama} menjadi {self.hp}')
    print(f'mengisi ulang Mana {self.nama} menjadi {self.mana}')
  
  def ultimate(self):
    print(f'Hero mengeluarkan skill ultimate!')

class fighter(hero):
  def __init__(self, nama, hp, mana, attack, defense):
    self.nama = nama
    self.hp = hp
    self.mana = mana
    self.attack = attack
    self.defense = defense
    self.max_hp = hp
    self.max_mana = mana

  def ultimate(self):
    print(f'{self.nama} mengeluarkan skill ultimate!')  # ultimate tanpa mana
    return self.attack * 4                              # rumus damage ultimate

class mage(hero):
  def __init__(self, nama, hp, mana, attack, defense):
    self.nama = nama
    self.hp = hp
    self.mana = mana
    self.attack = attack
    self.defense = defense
    self.max_hp = hp
    self.max_mana = mana
    
  def ultimate(self):
    if self.mana-100 >= 0:                       # ultimate perlu 100 mana
      print(f'{self.nama} mengeluarkan skill ultimate')
      self.mana -= 100                           # ultimate mengurangi 100 mana
      return self.attack * 4                     # rumus damage ultimate
    else:
      print(f'{self.nama} kehabisan mana!')
      return 0