import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class shm:
    def __init__(
            self, 
            mass: float, 
            spring_constant: float,
            initial_position: float , 
            initial_velocity : float,
            delta_time: float
        ) -> None:
        
        self.mass = mass
        self.spring_constant = spring_constant
        self.mass_position = initial_position
        self.mass_velocity = initial_velocity  
        self.mass_acceleration = 0.0
        self.delta_time = delta_time
        

    def calculate_spring_force(self) -> float:
        """ Beregner fjederkraften via Hookes lov: F = -k * x """
        return -self.spring_constant * self.mass_position
    
    def update_state(self) -> None:
        """ Opdaterer acceleration, hastighed og position """
        self.mass_acceleration = self.calculate_spring_force() / self.mass
        self.mass_velocity += self.mass_acceleration * self.delta_time
        self.mass_position += self.mass_velocity * self.delta_time
        pass
    
    def simulate(self, time: float) -> tuple:
        """ Simulerer systemet i en given tid """
        steps = int(time / self.delta_time)
        position = np.zeros(steps)
        velocity = np.zeros(steps)
        acceleration = np.zeros(steps)
        time_array = np.zeros(steps)
        
        for i in range(steps):
            self.update_state()
            position[i] = self.mass_position
            velocity[i] = self.mass_velocity
            acceleration[i] = self.mass_acceleration
            time_array[i] = i * self.delta_time
            
        return time_array, position, velocity, acceleration
    
    def create_simulation_C(self, time) -> None:
        fig, axs = plt.subplots(4, 1, figsize=(10, 8))
    
        time, pos, vel, acc = self.simulate(time=time)
        
        axs[0].plot(time, pos, label="Position [m]", color = 'blue')
        axs[0].set_title("Position")
        axs[0].set_xlabel("Tid (s)")
        axs[0].set_ylabel("Position (m)")
        axs[0].legend()
        axs[0].grid()
    
        axs[1].plot(time, vel, label="Hastighed [m/s]", color = 'green')
        axs[1].set_title("Hastighed")
        axs[1].set_xlabel("Tid (s)")
        axs[1].set_ylabel("Hastighed (m/s)")
        axs[1].legend()
        axs[1].grid()
    
        axs[2].plot(time, acc, label="Acceleration [m/s^2]", color='red')
        axs[2].set_title("Acceleration")
        axs[2].set_xlabel("Tid (s)")
        axs[2].set_ylabel("Acceleration (m/s^2)")
        axs[2].legend()
        axs[2].grid()
        
        axs[3].plot(time, pos, label="Position [m]", color='blue')
        axs[3].plot(time, vel, label="Hastighed [m/s]", color='green')
        axs[3].plot(time, acc, label="Acceleration [m/s^2]", color='red')
        axs[3].set_title("Kombineret plot")
        axs[3].set_xlabel("Tid (s)")
        axs[3].set_ylabel("Værdi")
        axs[3].legend()
        axs[3].grid()
    
        plt.tight_layout()
        plt.show()
        pass
    
    def create_simulation_D(self, m_values, k_values) -> None:
        # 3D-plot af svingningstid som funktion af m og k
        
        M, K = np.meshgrid(m_values, k_values)
        T = 2 * np.pi * np.sqrt(M / K)  # Svingningstid (T = 2π√(m/k))

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(M, K, T, c=T, cmap='viridis')
        ax.set_xlabel('Masse (kg)')
        ax.set_ylabel('Fjederkonstant (N/m)')
        ax.set_zlabel('Svingningstid (s)')
        ax.set_title('Svingningsperiode vs masse og fjederkonstant')
        plt.show()

        pass

if __name__ == "__main__":
    
    system = shm(
        mass=10,
        spring_constant=10, 
        initial_position=1, 
        initial_velocity=0.0, 
        delta_time=0.01
    )

    system.create_simulation_C(20)
    
    m_values = np.linspace(0.5, 5.0, 20)  # Mass range: 0.5 to 5 kg
    k_values = np.linspace(5.0, 20.0, 20)  # Spring constant range: 5 to 20 N/m
    
    system.create_simulation_D(m_values, k_values)

