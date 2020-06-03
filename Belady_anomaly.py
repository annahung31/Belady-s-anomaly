from collections import deque 
import matplotlib.pyplot as plt
import ipdb
def FIFO(capacity, ref_string):

    frames = deque([]) 
    page_fault = 0
    for page in ref_string:
        if page in frames:
            continue
        else:
            page_fault += 1
            if len(frames) < capacity:
                frames.append(page)
                #print("Appended %s"% str(page))
            else:
                removed = frames.popleft()
                #print('Removed  %s'% str(removed))
                frames.append(page)
                #print("Appended %s"% str(page))
    
    #print('page fault num = %s'%page_fault)
    return page_fault





def LFU(capacity, ref_string):
    counting = dict()
    frames = []
    page_fault = 0
    for page in ref_string:
        print('-'*20)
        print(counting)
        print(frames)
        print('page now: ', page)

        if page in frames:
            print('page already in frame: %s'%page)
            continue
        else:
            page_fault += 1
            if len(frames) < capacity:
                frames.append(page)
                print("Appended %s"% str(page))
            else:
                
                print('find min ',counting)
                least_freq = min(counting.values())
                least_used = counting.keys()[counting.values().index(least_freq)] 
                print('Removed  %s'% str(least_used))
                
                frames.remove(least_used)

                del counting[least_used]
                
                frames.append(page)
                print("Appended %s"% str(page))

        #count this page
        if page not in list(counting.keys()):
            counting[page] = 1
        else:
            counting[page] += 1


    return page_fault






if __name__ == '__main__':
    #reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4,5]
    #reference_string = [1,3,4,7,1,8,9,7,6,2,8,0]
    #reference_string = [2,4,1,5,1,0,7,3,1]
    #reference_string = [3,4,2,5,2,6,3,8,7,0,2,4,0,7,4]
    #reference_string = [2,3,4,3,2,4,3,2,4,5,6,7,5,6,7,4,5,6,7,2,1]
    reference_string = [1,2,3,4,5,3,4,1,6,7,8,7,8,9,7,8,9,5,4,5,4,2]
    capacitys = [3,4,5,6]
    pfs = []
    for capacity in capacitys:
        page_fault = FIFO(capacity, reference_string)
        pfs.append(page_fault)
    
    plt.bar(capacitys, pfs, color='lightblue')
    plt.xticks(capacitys,[str(x) for x in capacitys])
    plt.yticks(pfs,[str(y) for y in pfs])
    plt.xlabel('Capacity')
    plt.ylabel('Page Fault number')

    plt.savefig('FIFO_5.png')
    plt.show()
