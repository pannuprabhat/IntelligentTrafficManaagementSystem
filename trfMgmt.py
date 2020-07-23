import time
import cv2
import yolo_model as yolo
import hardware as hw
import os

max_green = 160 
total_green= 0
lane_time=[]
vehicle_count=[]
lane_status=[]
i=0 
net = yolo.call_yolo()

vs = yolo.get_video_streams()

def get_vehicle_count(lane_number):
    global vs 
    k=0
    while k<1 :
        rval, frame = vs[lane_number].read()
        k+=1
    count = yolo.get_vehicles(frame , net)
    
    return count

def set_lane_time():
    global vehicle_count
    global lane_time
    sum=0
    j=0
    
    while j<4 :
        sum=sum+vehicle_count[j]
        j+=1
    j=0

    total_green = setTotalTime(sum)


    while j<4 :
        lane_time[j]=int((((total_green*vehicle_count[j])/sum)+5))
        j=j+1


def setTotalTime (count):
    green = min(max_green ,count )
    return green
    
    

while i<4 :
    lane_time.append(0)
    vehicle_count.append(get_vehicle_count(i))
    lane_status.append(0)
    i=i+1

i=0
updateCount=0

totalVehicleCount =vehicle_count[0]
startTime = time.time()

while True:
    
    updateCount+=1
    hw.setLight(0) # turn orange 
    time.sleep(4)
    set_lane_time()
    i=i%4
    lane_status[i]=1
    hw.setLight(i+1)
    start=time.time()
    
    ## Set the lights on the device
    
    j =0 
    print ("\nUpdate number : %3d \n"%(updateCount))
    while j<4 :
        if(lane_status[j]==1):
            print ("THE LANE %2d IS GREEN, HAS TIME %3d AND VEHICLE COUNT IS %5d" % (j+1,lane_time[j],vehicle_count[j]))
        else :
            
            print ("THE LANE %2d IS RED, HAS TIME %3d AND VEHICLE COUNT IS %5d" % (j+1,lane_time[j],vehicle_count[j]))

        j+=1
    
    # Keep track of time in lanes 
    get_time_flag=0
    while  (int(time.time()-start)<=lane_time[i]-2) :
        if int(time.time()-start)>=lane_time[i]-10 and get_time_flag==0 :
            count=get_vehicle_count((i+1)%4)
            get_time_flag=1
        if get_vehicle_count(i)==0 :
            break
    lane_status[i]=0
    vehicle_count[(i+1)%4]=count  #update the next lane count
    
    if updateCount == 8 :
        timeTaken =time.time() -startTime
        print()
        print ("For 2 iterations :")
        print ("The total number of vehicle passed = %3d"% totalVehicleCount)
        print ("The total time taken by our solution = %3d"% timeTaken)
        print ("The time that would have been taken by existing system (40s per lane) = %3d"% (max_green*2))
        print ("Time saved by our solution = %3d"% (max_green*2 - timeTaken ))
        print ("Time saved in percentage = %3d percent "% (((max_green*2 - timeTaken )/max_green*2)*100))
        break

    totalVehicleCount += count    #update the total vehicle count to test the efficiency of the product
    i=i+1


    
    