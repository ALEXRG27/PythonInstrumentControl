import pyvisa
import numpy as np
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
print("This are the connected instruments")
print(rm.list_resources())
keithley = 0
PS = []
init = 1
for x in rm.list_resources():
    USB = "USB"
    GPIB = "GPIB"
    if USB in x or GPIB in x:
        print("Instrument with address")
        print(rm.list_resources(x)) #Print GPIB address
        my_instrument = rm.open_resource(x) #Open Visa session
        print(my_instrument.query('*IDN?')) #Request identificator

        if "E3631A" in my_instrument.query('*IDN?'): #If it is a PS add it's address into the PS array
            PS.append(rm.open_resource(x))
            print("Power supply",init, PS) #PS n° + GPIB address
            init = init + 1
        else:
            if "MODEL 2000" in my_instrument.query('*IDN?'):keithley = rm.open_resource(x)#If it is a multimeter asign it to keithley variable
            print(keithley)
    else:
        print("Not accessible!")#If not PS or multi = Not accessible
print("Initialized instrument")
print(rm.list_opened_resources())
print("My Power supply addresses are", PS)
print("My Multimeter addres is", keithley)
def Voltage_measurement_py():
    print("Reset multimeter")
    keithley.write("*rst; status:preset; *cls")
    interval_in_ms = 500
    number_of_readings = 10
    keithley.write("status:measurement:enable 512; *sre 1")
    keithley.write("sample:count %d" % number_of_readings)
    keithley.write("trigger:source bus")
    keithley.write("trigger:delay %f" % (interval_in_ms / 1000.0))
    keithley.write("trace:points %d" % number_of_readings)
    keithley.write("trace:feed sense1; trace:feed:control next")
    keithley.write("initiate")
    keithley.assert_trigger()
    keithley.wait_for_srq()
    voltages = keithley.query_ascii_values("trace:data?")
    print("Average voltage: ", sum(voltages) / len(voltages))
    keithley.query("status:measurement?")
    keithley.write("trace:clear; trace:feed:control next")
def Voltage_measurement():
    points = 10
    keithley.timeout = 100000 #enlarge timeout for number of points
    keithley.write("*RST;status:preset; *cls") #reset
    keithley.write(":FUNC 'VOLT:DC';:VOLT:DC:DIG 7;:VOLT:DC:NPLC 1.000000;:VOLT:DC:RANG:AUTO ON;:VOLT:DC:AVER:STAT OFF;:VOLT:DC:REF:STAT OFF;")
    keithley.write(":TRIG:SOUR IMM;:TRIG:COUN INF;:TRIG:DEL:AUTO OFF;:TRIG:DEL 0.000000;")
    keithley.write(":INIT:CONT ON;")
    keithley.write(":FORM:BORD NORM;:FORM ASC;:FORM:ELEM READ;:TRAC:POINTS {};:SAMP:COUN 1;:TRAC:FEED SENSE;:TRAC:CLE;:TRAC:FEED:CONT NEXT;".format(points))
    keithley.write("*SRE 1;:STAT:MEAS:ENAB 512;*CLS;")
    voltages = keithley.query_ascii_values("trace:data?")
    print(voltages)
    print("Average voltage: ", sum(voltages) / len(voltages))
    plt.plot(voltages)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
if keithley != 0: Voltage_measurement()
Supply=0
Voltage=3
def PowerSupplyON(Supply,Voltage):
    E3631A = PS[Supply]
    E3631A.query("*IDN?")
    E3631A.write("INST P6V") # Select +6V output
    E3631A.write("VOLT {}".format(Voltage)) # Set output voltage to 2.0 V
    E3631A.write("CURR 1.0")
    E3631A.write("OUTP ON")
    print(E3631A.query(":INST:NSEL 1;:MEAS:VOLT? "))
    print(E3631A.query(":INST:NSEL 1;:MEAS:CURR? "))
    #E3631A.write("OUTP ON")
if PS[Supply] != 0: PowerSupplyON(Supply,Voltage)