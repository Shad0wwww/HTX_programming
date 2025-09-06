

class PidController:
    def __init__(self, Kp, Ki, Kd, setpoint=0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.integral = 0
        self.previous_error = 0

    def calculate(self, measurement: float, dt: float) -> float:
        """
        Calculate PID output based on the setpoint and current measurement.
        :param measurement: Current measurement of the process variable.
        :param dt: Time interval since the last calculation.
        :return: Control output.
        """

        # Calculate PID output
        error = self.setpoint - measurement

        self.integral += error * dt

        proportional = self.Kp * error

        IntegralOutput = self.Ki * self.integral

        derivativeOutput = (self.Kd * (error-self.previous_error))
        self.previous_error = error

        # Compute total output
        output = proportional + IntegralOutput + derivativeOutput
        return output
