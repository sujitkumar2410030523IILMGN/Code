class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []    
        
        for asteroid in asteroids:
            if asteroid>0 or not st:
                st.append(asteroid)
            else:
                while st and st[-1]>0 and st[-1]< abs(asteroid):
                    st.pop()    
                if st and st[-1] == abs(asteroid):
                    st.pop()
                else:  
                    if not st or st[-1] <0:
                        st.append(asteroid)
        return st      


https://leetcode.com/submissions/detail/1952036636/
