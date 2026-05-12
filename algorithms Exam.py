# Write your CUSTOM search algorithm (a function) and an sorting algorithm (a function) AS DESCRIBED IN THE ASSIGNMENT INSTRUCTIONS here
# You MAY NOT USE any pre-built python functions

def linear_search(contact_list, target_first_name):
    
    for contact in contact_list:
        
        if contact.first_name.lower() == target_first_name.lower():

            return contact
        
        return None
    
    def bubble_sort(contact_list):

        n = len(contact_list)

        for i in range(n):

            for j in range(0,n - i - 1):
                
                if contact_list[j].last.name > contact_list[j + 1].last_name:

                    temp = contact_list[j]
                    contact_list[j] = contact_list[j + 1]
                    contact_list[j + 1] = temp

                return contact_list       
