class Carro():
    def __init__(self, vel_max):
        self.vel_max = vel_max
        self.vel_atual = 0

    def acelerar(self, passo=5):
        if self.vel_atual <= 180 - passo:
            self.vel_atual += passo
        else:
            self.vel_atual = 180
        return self.vel_atual

    def frear(self, passo=5):
        if self.vel_atual >= 0 + passo:
            self.vel_atual -= passo
        else:
            self.vel_atual = 0
        return self.vel_atual


if __name__ == '__main__':
    '''
    Esse parâmetro é a velocidade máxima
    A velocidade mínima é zero né
    '''
    c1 = Carro(180)

    for _ in range(25):
        '''
        O delta por padrão é 5
        Ao acelerar ele não pode passar de 180
        mas tem que chegar em 180
        '''
        vel_atual = f'A velocidade atual é de {c1.acelerar(8)} km/h.'
        print(vel_atual)

    for _ in range(10):
        '''
        O delta por padrão é 5
        Ao frear ele não pode passar de 0
        mas tem que chegar em 0
        '''
        vel_atual = f'A velocidade atual é de {c1.frear(passo=19)} km/h.'
        print(vel_atual)
