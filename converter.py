print("choose one option from below options:")
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
opt=int(input("option(1/2):"))
if(opt==1):
  c=float(input(" Enter Temperature in Celsius:"))
  f=1.8*(c)+32
  f=round(f,1)
  print("Temperature in Fahrenheit =",f)
elif(opt==2):
   f=float(input("Enter Temperature in Fahrenheit:"))
   c=(f-32)/1.8
   c=round(c,1)
   print("Temperature in Celsius =",c)
else:
   print("Choose 1 or 2")
