#' Script for merging all data files
#' Author: Marcel Kempenaar

read_sample <- function(file.name) {
  ## Extract the sample name for naming the column
  sample.name <- gsub(".txt", "", file.name)
  ## Read the data, setting the 'transcript_id' as row.names (column 1)
  sample <- read.table(file.name, header = FALSE, sep="\t", row.names = NULL)
  ## Rename the count column
  names(sample)[2] <- sample.name
  ## Return a subset containing the 'transcript_id' and sample name columns
  return(sample[c(1, 2)])
}

file.names <- list.files()

dataset <- read_sample(file.names[1])

for (file.name in file.names[2:length(file.names)]) {
  sample <- read_sample(file.name)
  dataset <- merge(dataset, sample, by = 1)
}

row.names(dataset) <- dataset$V1
dataset <- dataset[-1]

write.table(dataset, file="GSE144028.txt")