# libraries
# library(ggplot2)
# library(plyr)
# library(reshape2)

# copy the following so you can do sme()
WORKDIRECTORY='/work/directory'
THISFILE     ='thisfile.r'
setwd(WORKDIRECTORY)
sme <- function()
{
    setwd(WORKDIRECTORY)
    source(THISFILE)
}

explore.FSJ386323 <- function()
{
    transfer <- function()
    {
    }
    load <- function()
    {
    }

    clean <- function(d)
    {
    }

    func <- function(d)
    {
    }

    do_main <- function()
    {
        d = load()
        d = clean(d)
        func(d)
    }
    do_main()
}

main <- function()
{
    explore.FSJ386323()
}
main()
