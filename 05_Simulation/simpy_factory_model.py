"""
🚀 Industrial-Engineering-Hub: Systems Simulation
Factory Production Line Discrete Event Simulation (SimPy)
"""

import simpy
import random

# Simulation Parameters
RANDOM_SEED = 42
MACHINE_TIME = 5     # Minutes to process one part
OPERATOR_TIME = 2    # Minutes for operator to handle part
ARRIVAL_INTERVAL = 4 # Minutes between part arrivals
SIM_TIME = 100       # Minutes to run the simulation

class Factory(object):
    """
    A factory has a limited number of machines and operators.
    Parts must be processed by a machine and then handled by an operator.
    """
    def __init__(self, env, num_machines, num_operators):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.operator = simpy.Resource(env, num_operators)

    def process_part(self, part_name):
        """Standard manufacturing process."""
        print(f"📦 {part_name} istasyona geldi: {self.env.now:.2f}")
        
        # Step 1: Machining
        with self.machine.request() as request:
            yield request
            print(f"⚙️ {part_name} işlem görmeye başladı: {self.env.now:.2f}")
            yield self.env.timeout(MACHINE_TIME + random.uniform(-1, 1))
            print(f"✅ {part_name} işlemesi bitti: {self.env.now:.2f}")

        # Step 2: Operator Handling
        with self.operator.request() as request:
            yield request
            print(f"👤 Operatör {part_name} ile ilgileniyor: {self.env.now:.2f}")
            yield self.env.timeout(OPERATOR_TIME)
            print(f"🏁 {part_name} hattan çıktı: {self.env.now:.2f}")

def part_generator(env, factory):
    """Generates new parts that arrive at the factory."""
    for i in range(100): # Arrivals
        yield env.timeout(random.expovariate(1.0 / ARRIVAL_INTERVAL))
        env.process(factory.process_part(f"Parça-{i+1}"))

def main():
    print("--- 🏭 Endüstri Mühendisliği Karar Destek Sistemi: Fabrika Simülasyonu ---")
    print(f"Simülasyon parametreleri: Makine Süresi={MACHINE_TIME}, Operatör Süresi={OPERATOR_TIME}")
    
    # Setup and start the simulation
    random.seed(RANDOM_SEED)
    env = simpy.Environment()
    factory = Factory(env, num_machines=2, num_operators=1)
    
    env.process(part_generator(env, factory))

    # Run!
    print("🚀 Simülasyon başlatılıyor...\n")
    env.run(until=SIM_TIME)
    print("\n🏁 Simülasyon tamamlandı.")

if __name__ == "__main__":
    main()
