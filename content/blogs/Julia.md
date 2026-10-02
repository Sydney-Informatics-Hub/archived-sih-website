+++
redirectTo = "/news/julia"
date = "2019-05-08T00:00:00+10:00"
title = "Using Julia to transpose genomics data"
draft = false
type = "sidebar"
blog = true
stream = "news"

thumbnail = "/images/blog/tassie.png"
summary = "My first Julia Code beyond Hello World! "

authorname = "Nathaniel Butterworth"
authoravatar = "/people/NathanielButterworth.jpg"
authorbio = "Works in in the Research Computing team, plays with HPC, visualisation, general hacking."
+++


I went to an Intro to Julia course recently and I was immediately hooked. It seems to have the speed of C, the ease of writing and reading as Python, and the data wrangling abilities of R. Anyway, working with some nice data sets in the workshop is great, but I wanted a coding problem to test in the wild. Enter the Tasmanian Devil! 

I needed to perform a pretty simple task, transpose a matrix of data and simultaneously group the data. The data comes from [Carolyn Hogg](https://sydney.edu.au/research/people/carolyn.hogg.php) and [Catherine Grueber](https://sydney.edu.au/science/people/catherine.grueber.php), two researchers trying to understand and preserve our cute little Tasmanian Devils.  I could have done this easily in my go-to language Python, but I resisted the urge as I thought this was a neat little problem to test my newly acquired Julia skills. And thankfully there are plenty of stackoverflow articles already written for me to learn from! 

So let's see what I did. 

Firslty, load in the packages we will need (equivalent to import in Python) 

```python 
using DelimitedFiles 
``` 

Next read in the transposed genotype file, loci in rows, individual Tasmanian devils in column pairs: 
```python 
fname="25_devils_maf05_geno20.tped" 
f = readdlm(fname) 
``` 

The data input should look like this: 
``` 
1403557×54 Array{Any,2}: 
0  "NW_003846419.1:4"        0  …   "A"   "A"   "A"   "T"  0     0    
0  "NW_003834869.1:5"        0     0     0      "C"   "C"   "C"   "C" 
0  "NW_003836027.1:6"        0      "C"   "T"   "C"   "T"   "T"   "T" 
⋮                               ⋱              ⋮                      
0  "NW_003831915.1:5201973"  0  …   "T"   "T"   "T"   "T"   "T"   "T" 
0  "NW_003831915.1:5270994"  0  …   "C"   "C"   "T"   "C"   "C"   "C" 
0  "NW_003831915.1:5271029"  0      "T"   "T"   "T"   "T"   "C"   "T" 
0  "NW_003831915.1:5279631"  0      "G"   "G"   "G"   "T"   "T"   "T" 
``` 

That is a 70Mb file, with 1403557 rows (loci/SNPS) and 54 columns (individuals). Now initialise a blank array to fill with 1's,0's and NA's, we will now have individuals in rows, loci in columns: 
```python 
hzsmat = Array{String}(undef, Int((size(f)[2]-4)/2),size(f)[1]) 
``` 

Our new hzsmat variable (heterozygosity matrix) looks like this: 
``` 
25×1403557 Array{String,2}: 
#undef  #undef  #undef  #undef  #undef  …  #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef  …  #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
#undef  #undef  #undef  #undef  #undef     #undef  #undef  #undef  #undef 
``` 

Now for the fun stuff. There are probably more elegant ways to do this, but I am just doing some classic nested for-loops here. So, loop through all loci in the file: 
```python 

start = time() 

#Loop through all loci in the file 
for j in 1:size(f)[1] 
    #Loop through individuals in each row of the loci 
    #Indiduals are paired in columns 
    #hzsmat is transposed form the original data 

    for (i,letterpair) in enumerate(f[j,5:2:end]) 
        #print(i," ", letterpair," ") 
        #print(f[j,5+i*2-1], "\n") 
        
        #If the genotype is “0 0”, code this as NA. 
        if letterpair == 0 || f[j,5+i*2-1] == "0" 
            #print("NA") 
            hzsmat[i,j]="NA" 

        #if the alleles are the same (A A, C C, G G or T T),  
        #code this as 0 to indicate a “homozygous” genotype 
        elseif letterpair == f[j,5+i*2-1] 
            #print("0") 
            hzsmat[i,j]="0" 

        #If the alleles in the genotype are different  
        #code this as 1 to indicate the a “heterozygous” genotype 
        else letterpair != f[j,5+i*2-1] 
            #print("1") 
            hzsmat[i,j]="1" 

        end          

    end     

end 

elapsed = time() - start 

#And save out the data 
writedlm("FileName.csv",  hzsmat,','); 
``` 

Elapsed time is ***48.48463702201843*** seconds! Hey, not too bad I think. It is a pretty mundane task and I only have to do it once. But, just because it is fun I obviously want to see if I can speed things up by trying Julia's multi-threading capabilities. This is pretty straightforward to make the changes. 

Firstly, we have to set some parameters in our Bash environment before we start Julia... 
``` 
export JULIA_NUM_THREADS=4 
``` 

Launch Julia again and see how many threads are available to us 
``` 
Threads.nthreads() 
``` 

And yes, the answer is 4! A good start. Now to re write our nested for-loops: 
```julia 

start = time() 

#Loop through all loci in the file 
Threads.@threads for j in 1:size(f)[1]  
    #Loop through individuals in each row of the loci 
    #Indiduals are paired in columns 
    #hzsmat is transposed form the original data 
    for (i,letterpair) in enumerate(f[j,5:2:end]) 
        #print(i," ", letterpair," ") 
        #print(f[j,5+i*2-1], "\n") 

        #If the genotype is “0 0”, code this as NA. 
        if letterpair == 0 || f[j,5+i*2-1] == "0" 
            #print("NA") 
            hzsmat[i,j]="NA" 

        #if the alleles are the same (A A, C C, G G or T T),  
        #code this as 0 to indicate a “homozygous” genotype 
        elseif letterpair == f[j,5+i*2-1] 
            #print("0") 
            hzsmat[i,j]="0" 

        #If the alleles in the genotype are different  
        #code this as 1 to indicate the a “heterozygous” genotype 
        else letterpair != f[j,5+i*2-1] 
            #print("1") 
            hzsmat[i,j]="1" 
            
        end 

    end    

end 

elapsed = time() - start 
``` 

And the result.... Elapsed time is ***47.88510298728943*** seconds. Wow, what am I going to do with all my free time ¯\_(ツ)_/¯ 
  
So I didn't get the immediate speed up I was hoping for. But this was a fun little exercise for my first introduction to the  Julia language. 


Interested in learning Julia or more about HPC and programming? Our training partners [Intersect](https://intersect.org.au/) run the course following the [Software Carpentry](https://software-carpentry.org/lessons/) style format. And check out our calendar to see the [upcoming training session](https://informatics.sydney.edu.au/training/#calendar). 


So, the next step is processing this output with R (does no one use Python anymore >_<). Really, being language agnostic would be great, but it is so hard to resit the temptation just to pick up Python everytime I have a problem! Check for another blog post coming soon! 

Get in touch if you have any comments, questions, or abuse: nathaniel.butterworth@sydney.edu.au 

 
