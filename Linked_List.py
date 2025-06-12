"""
🎙️ Linked List: It is a Linear Data Structure where each element is called a node and it contains 2 fields

      ◎ Data field: It is used to store element/information
      ◎ Address/ Next field: It is used to store the address of the next node
      
  It mainly allows efficient insertion and deletion operations compared to arrays. 



🎙️ Types:
      ◎ Single Linked List
      ◎ Double Linked List
      ◎ Circular Linked List
      ◎ 




 	Array				Vs	 	Linked List
---------------------------------------------------------------------------------
◎ fixed size						◎ Dynamic

◎ Efficient while					◎ It is not that efficient
  accessing an element					  while accessing an element

◎ Inserting and deleting				◎ Inserting  and deleting middle
  the middle element takes 				   element take less time O(1)
  more time



    
🎙️ Creating a Node:
   code:
          class Node:
              def __init__(self, data):
                  self.data = data
                  self.next = None


🎙️ Creating a Single Linked List:
   code:
         



      
🎙️ Operations on Single Linked List:

      ◎ Traversing: 
      
            ◎ It is used to traverse only single and double linked list
            Code:
                  def Traverse(head):
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
                            


      ◎ Searching: Traverse a linked list to search an element/Key
       code:
                  def Searching(head, key):
                        temp = head
                        while temp is not None:
                              if temp.data == key:
                                    return True
                              temp = temp.next
                        return False


                              
      ◎ Insertion: While doing insertion we check 2 cases there are:
      
            case-1: If the linked list has no nodes
            case-2: If linked list has a nodes


              ◎ def Insert_at_beg(head, data):
                    new_node = Node(data)     # data is transformed into node
                    new_node.next = head 
                    return new_node


                          
              ◎ def Insert_at_last(head, data):
                    new_node = Node(data)     # data is transformed into node
                    
                    if head is None:
                        return new_node       
                    temp = head
                    while temp.next:     #  Traverse till the last node
                          temp = temp.next
                    temp.next = new_node
                    return head


                    
              ◎ def insert_at_kth_position(head, k, data):
                      new_node = Node(data)     # data is transformed into node
                      
                      if k == 1:
                          new_node.next = head
                          return new_node
                          
                      current = head
                      count = 1
                      while current and count < k - 1:
                          current = current.next
                          count += 1
                          
                      if not current:
                          return head
                      new_node.next = current.next
                      current.next = new_node
                      return head


            
      ◎ Reverse of a Linked list:
      code:
                  def reverse_linked_list(head):
                      prev = None
                      current = head
                  
                      while current:
                          next_node = current.next  # store next
                          current.next = prev       # reverse the link
                          prev = current            # move prev to current
                          current = next_node       # move to next node
                  
                      return prev  # new head



        ◎ Deletion: While doing deletion we check 3 cases there are:
 
            case-1: If the linked list has no nodes
            case-2: single-node in linked list
            case-3: linked list has mutiple node


               ◎ def delete_at_start(head):
                      if not head:
                          return None
                      return head.next
 

            
               ◎   def delete_at_end(head):
                      if not head or not head.next:
                          return None
                      current = head
                      while current.next.next:
                          current = current.next
                      current.next = None
                      return head



               ◎ def delete_at_kth_position(head, k):
                      if not head:
                          return None
                      if k == 1:
                          return head.next
                      current = head
                      count = 1
                      while current.next and count < k - 1:
                          current = current.next
                          count += 1
                      if not current.next:
                          return head
                      current.next = current.next.next
                      return head


"""
