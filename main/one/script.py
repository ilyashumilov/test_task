
from models import *

class script:
    @staticmethod
    def main():
        result = {}
        sellers = user.objects.filter(role="seller")
        for i in sellers:
            buyers = {}
            lots = lot.objects.filter(seller = i)

            for n in lots:
                for m in deal.objects.filter(lot = n):
                    if m.buyer.name not in buyers:
                        buyers[m.seller] = 0
                    try:
                        buyers[m.seller] += m.amount * m.lot.price
                    except:
                        pass

            result[i] = buyers

        return result

if __name__ == '__main__':
    print(script.main())