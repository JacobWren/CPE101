# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Moonlander Project
# Term:         Winter 2020




def main():
    show_welcome()
    get_altitude_ = get_altitude()
    get_fuel_ = get_fuel()
    display_state(0, get_altitude_, 0, get_fuel_, 0)
    f_r = get_fuel_rate(get_fuel_)
    time = 0
    z = update_fuel(get_fuel_, 0)
    p = update_velocity(0, 0)
    #p_not = update_velocity(0, 0)
    q = update_acceleration(1.62, f_r)
    #k = update_altitude(get_altitude_, p, q)
    k = get_altitude_
    
    #l = [0]
    #n = -1
    while k > 0:
        #n = n + 1
        z = update_fuel(z, f_r)
        k = update_altitude(k, p, update_acceleration(1.62, f_r))
        p = update_velocity(p, update_acceleration(1.62, f_r))
        
        
        #l.append(p)
        #k = update_altitude(k, l[n], update_acceleration(1.62, f_r))
        
        
        time = time + 1
        if z < 0:
           z = 0
        display_state(time, k, p, z, f_r)
        if k == 0:
            display_landing_status(p)
        if z > 0 and k > 0:
            #p_not = update_velocity(p_not, update_acceleration(1.62, f_r))
            #f_r = min(get_fuel_rate(get_fuel_), z)
            f_r = get_fuel_rate(z)
        else:
            f_r = 0
    
     
def show_welcome() -> None:
    print("\nWelcome aboard the Lunar Module (LM) Flight Simulator!\n")
    print("  To begin, provide an initial altitude and fuel amount.")
    print("  To simulate the actual LM, use 1300 meters and 500 liters.\n")
    
    
    
def get_fuel() -> int:
    fuel = int(input("Enter initial fuel amount (in liters): "))
    while fuel < 1:
        print("[ERROR] Fuel amount must be positive")
        fuel = int(input("Enter initial fuel amount (in liters): "))
    return fuel
    

def get_altitude() -> int:
    altitude = int(input("Enter initial altitude (1 to 9999 meters): "))
    while altitude < 1 or altitude > 9999:
        print("[ERROR] Altitude out of range")
        altitude = int(input("Enter initial altitude (1 to 9999 meters): "))
    return altitude
        
    
def get_fuel_rate(fuel_amount: int) -> int:
    fuel_rate = int(input("Enter fuel rate (0 to 9 liters per second): "))
    while fuel_rate < 0 or fuel_rate > 9:
        print("[ERROR] Fuel rate out of range")
        fuel_rate = int(input("Enter fuel rate (0 to 9 liters per second): "))
    return min(fuel_amount, fuel_rate)

        
    
    
def update_fuel(fuel_amount: int, fuel_rate: int) -> int:
    fuel_Now = fuel_amount - fuel_rate
    if fuel_Now < 0:
        fuel_Now = 0
    return fuel_Now
        
        
def update_acceleration(gravity: float, fuel_rate: int) -> float:
    acceleration = gravity * ((fuel_rate / 5) - 1)
    return acceleration
        

def update_velocity(velocity: float, acceleration: float) -> float:
    velocity = velocity + acceleration 
    return velocity
        


def update_altitude(altitude: float,
                    velocity: float,
                    acceleration: float) -> float:
    altitude = altitude + velocity + (acceleration / 2)
    if altitude < 0:
        altitude = 0
    return altitude



# f"{variable:width.#f}"
def display_state(time: int,
                  altitude: float,
                  velocity: float,
                  fuel_amount: int,
                  fuel_rate: int) -> None:
    #if fuel_amount < 0:
        #fuel_amount == 0
    if altitude <= 0:
        print()
        print("LM state at landing/impact")
        print("    Time: {0:4} s\n    Fuel: {1:4} l\n    Rate: {2:4} l/s\nAltitude: {3:7.2f} m\nVelocity: {4:7.2f} m/s".format(time, fuel_amount, fuel_rate, altitude, velocity))
        #print("    Fuel: {0:4} l".format(fuel_amount))
        #print("    Rate: {0:4} l/s".format(fuel_rate))
        #print("Altitude: {0:7.2f} m".format(altitude))
        #print("Velocity: {0:7.2f} m/s".format(velocity))
        print()
    elif time == 0:
        print()
        print("LM state at retrorocket cutoff")
        print("    Time: {0:4} s\n    Fuel: {1:4} l\n    Rate: {2:4} l/s\nAltitude: {3:7.2f} m\nVelocity: {4:7.2f} m/s".format(time, fuel_amount, fuel_rate, altitude, velocity))
        print()
    elif fuel_amount <= 0:
            print("[OUT OF FUEL]", f"Time: {time: 4}", f"Altitude: {altitude:7.2f}", f"Velocity: {velocity: 7.2f}")
    else:
        print("    Time: {0:4} s\n    Fuel: {1:4} l\n    Rate: {2:4} l/s\nAltitude: {3:7.2f} m\nVelocity: {4:7.2f} m/s".format(time, fuel_amount, fuel_rate, altitude, velocity))
        print()

        



def display_landing_status(velocity: float) -> None:
    if -1 <= velocity <= 0:
        print("[LANDING STATUS] The Eagle has landed!")
    elif -10 < velocity < -1:
        print("[LANDING STATUS] Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("[LANDING STATUS] Ouch, that hurt!")
        


# no additional code below this line
if __name__ == "__main__":
    main()
