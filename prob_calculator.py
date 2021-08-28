import copy
import random

class Hat:
  def __init__(self, **kwargs):  #{red:3, blue:2}
    self.contents = []
    for key, value in kwargs.items():
      aaa = 0
      while value > aaa:
        self.contents.append(key)
        aaa += 1    
        #self.contents = ['red','red','red','blue','blue']
  
  def drawn(self, num_of_balls_drawn):
    removed = []
    if num_of_balls_drawn > len(self.contents):
      return self.contents
    
    removed.append(random.sample(self.contents, num_of_balls_drawn))
    #removed = [['red','blue']]
    
    all_removed = (removed[0])
    #all_removed = ['red','blue']
    
    for ball in all_removed:
      self.contents.remove(ball)
    # Não sei porque isso é necessário, mas o teste pedia.
    
    return all_removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for experimento in range(num_experiments):
    expected_balls_copy = copy.deepcopy(expected_balls) 
    hat_copy = copy.deepcopy(hat) 
    balls_removed = hat_copy.drawn(num_balls_drawn) 
# o copy é necessário para sempre começarmos um novo experimento com as mesmas variáveis, ou seja, do mesmo ponto de partida.
# deep copy foi feito para fazer uma cópia da original e caso seja feita qualquer mudança na cópia, a original não será alterada.    
    for ball in balls_removed:
      if ball in expected_balls_copy:
        expected_balls_copy[ball] -= 1
# se foi retirada uma bola azul, no dicionário das bolas esperadas, o valor da chave azul diminuirá 1.
    for k, v in expected_balls_copy.items():
      if expected_balls_copy[k] <= 0:
        expected_balls_copy[k] = True
      else:
        expected_balls_copy[k] = False
# caso todas as bolas forem retiradas o mesmo numero de vezes que o esperado (ou mais), a key se tornará True
# se forem esperadas 3 bolas azuis e somente duas forem retiradas, a key('azul') não se tornará true
    if all(expected_balls_copy.values()):
      successes += 1
# se todas as keys forem True, podemos dizer que esse experimento foi um sucesso.  
  return successes / num_experiments



      

      