class Solution(object):
    def isPalindrome(self, s):
        # Step 1: Convert to lowercase
        processed = s.lower()

        # Step 2: Remove unwanted characters (like ':')
        cleaned = ""
        for ch in processed: # keep letters and digits only
            if ch.isalnum():  
                cleaned += ch
            # Step 3: Check if it's a palindrome
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False