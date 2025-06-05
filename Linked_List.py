"""
🎙️ Linked List: It is a Linear Data Structure where each element is called a node and it contains 2 fields

      ◎ Data field: It is used to store element/information
      ◎ Address/ Next field: It is used to store the address of the next node



🎙️ Types:
      ◎ Single Linked List
      ◎ Double Linked List
      ◎ Circular Linked List
      ◎ 




 			Array							    	Vs					  Linked List
---------------------------------------------------------------------------------
		 ◎ fixed size											      ◎ Dynamic

	   ◎ Efficient while								     	◎ It is not that efficient
			accessing an element							      while accessing an element

		 ◎ Inserting and deleting				        ◎ Inserting  and deleting middle
			 the middle element takes 						  element take less time O(1)
			 more time



    
🎙️ Creating a Node:
   code:
          class Node:
              def __init__(self, data, next = None):
                  self.data = data
                  self.next = next


🎙️ Creating a Single Linked List:
   code:
         



      
🎙️ Operations on Single Linked List:

      ◎ Traversing: 
            ◎ It is used to traverse only single and double linked list
            Code:
                  temp = head
                  while temp is not None:
                      print(temp.data)
                      temp = temp.next


            ◎ For circular Linked List Traverse we use:
            Code:
                    temp = head
                    if temp:
                        while True:
                            print(temp.head)
                            temp = temp.next
                            if temp == head:
                                break
                            

      ◎ Searching
      ◎ Insertion
      ◎ Deletion
"""
