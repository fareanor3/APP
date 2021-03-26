# What we were to produce

The subject is based on the data contained in the file https://www.data.gouv.fr/fr/datasets/r/554590ab-ae62-40ac-8353-ee75162c05ee, which you are asked to download (in the same folder as this notebook).the aim of the APP is to provide algorithms allowing to sort the communes of France according to certain criteria. The data are in .csv (comma separated values) format. You have to import these data in a python script namedénumero_groupe_APP1.pyYou have to implement algorithms to sort the communes of France by increasing order of distance to a given city. The goal is to propose the fastest algorithm possible. The implementation you will propose must not use either the sorted or the sort function. Your program will also give the following statistics: min (closest city to the city passed in parameter), first quartile, median, max. The implementation of a function giving the order quantile could be useful (reminder: the median is the quantile of order 12, for example).when the reference city is the first district of Paris, a possible (but not obligatory) output is: min: 0. 82 km for PARIS 02 (75002)first quartile : 187.15 km for PONT SUR SAMBRE (59138)median : 318.88 km for BELLEFONTAINE (88370)third quartile : 459.81 km for QUEYSSAC (24140)max : 9422.32 km for ST PHILIPPE (97442)You will be confronted with choices. Do not hesitate to explore the data with a spreadsheet.

>  ## APA Learning Objectives (AAV): upon completion of the "RETURN" session of this APA, each student should be able to.... 

- Explain or restate the definitions of the concepts of stability and in-place memory management. 
- Characterize a sort according to its stability and memory management.
- Create a sorting algorithm in Python from a pseudo-code algorithm.
- Evaluate a sorting program by modifying it to count the number of comparisons made.
- Estimate the duration of the application of a sorting algorithm as a function of the number of elements to sort
- Express the time complexity of an algorithm written in Python
- Choose an algorithm among others knowing only their complexity with the notation 
- Choose, among those they have studied, the most relevant algorithm according to the number of data and the type of data to process.
- Justify the choice of a sort.
- Compare experimentally two sorting algorithms.
- Identify the worst case and the best case for a sorting algorithm.
- Empirically evaluate the number of operations of an algorithm as a function of the number of input data.
- Determine theoretically the complexity with the Landau notation of an algorithm as a function of the number of input data.
- Define what is the space or time complexity of an algorithm.
- Predict the computation time of a sorting algorithm as a function of the number of elements.
