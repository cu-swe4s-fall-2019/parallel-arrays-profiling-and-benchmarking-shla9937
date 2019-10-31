# Hash tables
The first test I did was to try test the hash functions themselves. I started by hashing the words in rand_words.txt using h_ascii hashing. When I did that I seemed to get non random hashes.

![](ascii_hash_function_rand.png)

When I switch to a rolling hash the data actaully look uniform. 

![](rolling_hash_function_rand.png)

If I use non-random words I'd expect to see that the hashing is even worse for the Ascii and there is some pattern in the rolling hashes now.

![](rolling_hash_function_non_rand.png)

This is actually still pretty random, this seems like a robust type of hashing.

![](ascii_hash_function_non_rand.png)

This got really bad, you would not want to use this. 

Then I wanted to see if actually building a hash table was faster with linear or chain probing. So, I tried using using the rolling hash method with eith collison avoidance, I found that chain collison avoidance seemed  faster, and didn't deteriorate when you got near the length of the table.

![](rolling_linear.png) ![](rolling_chain.png)

Using random words seems to give you a lot less uniform time to insertion, which isn't particularlly suprising as the system would have to search through and find the right spot to insert.

![](rolling_chain_rand.png)

