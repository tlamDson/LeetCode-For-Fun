def topKFrequent(nums,k):
    if k == 0 | k <0:
        return []
    my_dict = {}
    for num in nums:
        my_dict[num] = my_dict.get(num,0) + 1
    my_dict_list = list(my_dict.items())
    my_dict_list.sort(key=lambda x: x[1],reverse=True)
    answer= []
    for index,item in enumerate(my_dict_list):
        if index < k :
            answer.append(item[0])
            print(answer)
    return answer

       
   
  
       

   
        
  

nums = [1,2,2,3,3,3]
topKFrequent(nums,3)