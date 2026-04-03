

# ---

# ## 🧾 Question 2 (Expected O(1))

# In the Kingdom of Arithmoria, a ritual staircase has **n glowing steps**. The first step emits energy **1**, the second **2**, the third **3**, and so on.

# To activate the royal beacon, the **total cumulative energy** of all **n steps** must be calculated.

# However, due to time constraints, the calculation must be performed in **constant time**.

# Compute the total energy emitted by the staircase.

# ---

# ## 📥 Input

# * An integer **n** representing the number of steps

# ---

# ## 📤 Output

# * Print a single integer representing the **total cumulative energy**

# ---

# ## 🧪 Sample Test Cases

# ### Case 1

# **Input:**

# ```text
# n = 1
# ```

# **Output:**

# ```text
# 1
# ```

# ---

# ### Case 2

# **Input:**

# ```text
# n = 5
# ```

# **Output:**

# ```text
# 15
# ```

# ---

# ### Case 3 (Large Constraint)

# **Input:**

# ```text
# n = 1000000000
# ```

# **Output:**

# ```text
# 500000000500000000


n= int(input().strip())
result = n*(n+1)//2
print(result)



