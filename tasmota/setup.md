# Tasmota Configuration for Supervisor

## Hardware

Relay 1 - Controller and Payload-Power.
Relay 2 - Motor driver power
Relay 3 - AUX

Switch 1 - USB-Power detect from main controller
Button 4 - Function button

Switch 5 through 12 - Bumper input


## Config

Execute the below commands to configure controller.

### Decouple buttons from Relays

```
SetOption73 1
```

### Set switches to not toggle, but transmit actual state

```
SwitchModeX 1
```

### Turn off robot power 30 seconds after main power via USB is lost

```
Rule1 ON switch1#state=1 DO Backlog Power1 on; ruletimer1 0 ENDON
ON switch1#state=0 DO ruletimer1 30 ENDON
ON rules#timer=1 DO Power1 0 ENDON
```

### Enable bumper switches to trigger and release relay

```
Rule2
ON switch5#state=0 DO sub1 1 ENDON 
ON switch6#state=0 DO sub1 1 ENDON 
ON switch7#state=0 DO sub1 1 ENDON 
ON switch8#state=0 DO sub1 1 ENDON 
ON switch9#state=0 DO sub1 1 ENDON 
ON switch10#state=0 DO sub1 1 ENDON 
ON switch11#state=0 DO sub1 1 ENDON 
ON switch12#state=0 DO sub1 1 ENDON 
ON switch5#state=1 DO add1 1 ENDON 
ON switch6#state=1 DO add1 1 ENDON 
ON switch7#state=1 DO add1 1 ENDON 
ON switch8#state=1 DO add1 1 ENDON 
ON switch9#state=1 DO add1 1 ENDON 
ON switch10#state=1 DO add1 1 ENDON 
ON switch11#state=1 DO add1 1 ENDON 
ON switch12#state=1 DO add1 1 ENDON 
ON Var1#state != 0 DO Power2 off ENDON 
ON Var1#state == 0 DO Power2 on ENDON 
```

### Keep serial loggin active

```
Rule3
ON Time#Minute|5 DO SerialLog 2 ENDON
```
