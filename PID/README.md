# PID Controller

A **PID controller** (Proportional–Integral–Derivative controller) is a control loop mechanism widely used in industrial control systems. It calculates an error value as the difference between a desired setpoint and a measured process variable, and applies correction based on proportional, integral, and derivative terms.

## Formula

The PID control algorithm is typically expressed as:

```
u(t) = K_p e(t) + K_i ∫ e(t) dt + K_d (de(t)/dt)
```

- **u(t)**: Control output
- **e(t)**: Error (setpoint - process variable)
- **K_p**: Proportional gain
- **K_i**: Integral gain
- **K_d**: Derivative gain

## Usage

PID controllers are used in applications such as:
- Temperature control
- Motor speed regulation
- Robotics
- Process automation

## Resources

- [Wikipedia: Proportional–integral–derivative controller](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller)

