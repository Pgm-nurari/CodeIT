def bike_car(vehicles, wheels):
    # t + f = v
    # 2t + 4f = w
    # 2v + 2f = w
    
    f = wheels//2 - vehicles
    t = vehicles - f
    return [t,f]

def main():
    print(bike_car(200,540))

if __name__=='__main__':
    main()