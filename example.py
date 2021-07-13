from abc import ABCMeta, abstractmethod

#抽象クラス
class Charactor(metaclass=ABCMeta):
    @abstractmethod
    def printJob(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defence(self):
        pass

    def strike(self):
        self.printJob()
        self.attack()
        self.attack()
        self.attack()
    
    def attack_and_defence(self):
        self.printJob()
        self.attack()
        self.defence()

class Wizard(Charactor):
    def printJob(self):
        print("魔法使い ----------")
    
    def attack(self):
        print("サンダーを唱えた")
    
    def defence(self):
        print("防壁を出現させた")

class Solider(Charactor):
    def printJob(self):
        print("戦士 ----------")
    
    def attack(self):
        print("相手に切りかかった")
    
    def defence(self):
        print("盾を構えた")

if __name__=='__main__':
    wizard = Wizard()
    wizard.strike()
    wizard.attack_and_defence()

    solider = Solider()
    solider.strike()
    solider.attack_and_defence()
    