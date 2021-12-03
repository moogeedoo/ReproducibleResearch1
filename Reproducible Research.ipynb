{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "It is now possible to collect a large amount of data about personal movement using activity monitoring devices such as a Fitbit, Nike Fuelband, or Jawbone Up. These type of devices are part of the “quantified self” movement - a group of enthusiasts who take measurements about themselves regularly to improve their health, to find patterns in their behavior, or because they are tech geeks. But these data remain under-utilized both because the raw data are hard to obtain and there is a lack of statistical methods and software for processing and interpreting the data.\n",
    "\n",
    "This assignment makes use of data from a personal activity monitoring device. This device collects data at 5 minute intervals through out the day. The data consists of two months of data from an anonymous individual collected during the months of October and November, 2012 and include the number of steps taken in 5 minute intervals each day.\n",
    "\n",
    "Data\n",
    "The data for this assignment can be downloaded from the course web site:\n",
    "\n",
    "Dataset: Activity monitoring data [52K]\n",
    "The variables included in this dataset are:\n",
    "\n",
    "steps: Number of steps taking in a 5-minute interval (missing values are coded as NA)\n",
    "\n",
    "date: The date on which the measurement was taken in YYYY-MM-DD format\n",
    "\n",
    "interval: Identifier for the 5-minute interval in which measurement was taken\n",
    "\n",
    "The dataset is stored in a comma-separated-value (CSV) file and there are a total of 17,568 observations in this dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solution\n",
    "Setting global options and loading required libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "also installing the dependencies 'xfun', 'tinytex', 'cli', 'rlang', 'rmarkdown', 'googlesheets4', 'reprex'\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "  There are binary versions available but the source versions are later:\n",
      "              binary source needs_compilation\n",
      "xfun            0.22   0.28              TRUE\n",
      "tinytex         0.31   0.35             FALSE\n",
      "cli            2.5.0  3.1.0              TRUE\n",
      "rlang         0.4.11 0.4.12              TRUE\n",
      "rmarkdown        2.8   2.11             FALSE\n",
      "googlesheets4  0.3.0  1.0.0             FALSE\n",
      "reprex         2.0.0  2.0.1             FALSE\n",
      "\n",
      "  Binaries will be installed\n",
      "package 'xfun' successfully unpacked and MD5 sums checked\n",
      "package 'cli' successfully unpacked and MD5 sums checked\n",
      "package 'rlang' successfully unpacked and MD5 sums checked\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "\"cannot remove prior installation of package 'rlang'\"Warning message in file.copy(savedcopy, lib, recursive = TRUE):\n",
      "\"problem copying C:\\Users\\nytro\\anaconda3\\Lib\\R\\library\\00LOCK\\rlang\\libs\\x64\\rlang.dll to C:\\Users\\nytro\\anaconda3\\Lib\\R\\library\\rlang\\libs\\x64\\rlang.dll: Permission denied\"Warning message:\n",
      "\"restored 'rlang'\""
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "package 'tidyverse' successfully unpacked and MD5 sums checked\n",
      "\n",
      "The downloaded binary packages are in\n",
      "\tC:\\Users\\nytro\\AppData\\Local\\Temp\\Rtmp6VNULo\\downloaded_packages\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "installing the source packages 'tinytex', 'rmarkdown', 'googlesheets4', 'reprex'\n",
      "\n",
      "Warning message in install.packages(\"tidyverse\"):\n",
      "\"installation of package 'tinytex' had non-zero exit status\"Warning message in install.packages(\"tidyverse\"):\n",
      "\"installation of package 'googlesheets4' had non-zero exit status\"Warning message in install.packages(\"tidyverse\"):\n",
      "\"installation of package 'rmarkdown' had non-zero exit status\"Warning message in install.packages(\"tidyverse\"):\n",
      "\"installation of package 'reprex' had non-zero exit status\""
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "  There is a binary version available but the source version is later:\n",
      "        binary source needs_compilation\n",
      "ggplot2  3.3.3  3.3.5             FALSE\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "installing the source package 'ggplot2'\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "  There is a binary version available but the source version is later:\n",
      "           binary source needs_compilation\n",
      "data.table 1.14.0 1.14.2              TRUE\n",
      "\n",
      "  Binaries will be installed\n",
      "package 'data.table' successfully unpacked and MD5 sums checked\n",
      "\n",
      "The downloaded binary packages are in\n",
      "\tC:\\Users\\nytro\\AppData\\Local\\Temp\\Rtmp6VNULo\\downloaded_packages\n",
      "\n",
      "  There is a binary version available but the source version is later:\n",
      "      binary source needs_compilation\n",
      "knitr   1.33   1.36             FALSE\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "installing the source package 'knitr'\n",
      "\n"
     ]
    }
   ],
   "source": [
    "install.packages(\"tidyverse\")\n",
    "install.packages(\"ggplot2\")\n",
    "install.packages(\"data.table\")\n",
    "install.packages(\"knitr\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "\"package 'data.table' was built under R version 3.6.3\"Warning message:\n",
      "\"package 'dplyr' was built under R version 3.6.3\"\n",
      "Attaching package: 'dplyr'\n",
      "\n",
      "The following objects are masked from 'package:data.table':\n",
      "\n",
      "    between, first, last\n",
      "\n",
      "The following objects are masked from 'package:stats':\n",
      "\n",
      "    filter, lag\n",
      "\n",
      "The following objects are masked from 'package:base':\n",
      "\n",
      "    intersect, setdiff, setequal, union\n",
      "\n"
     ]
    }
   ],
   "source": [
    "library(knitr)\n",
    "library(ggplot2)\n",
    "library(data.table)\n",
    "library(dplyr)\n",
    "opts_chunk$set(echo = TRUE, results = 'hold')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Loading the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "if(!file.exists(\"./data\")){dir.create(\"./data\")}\n",
    "fileUrl <- \"https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2Factivity.zip\"\n",
    "download.file(fileUrl,destfile=\"./data/activity.zip\",method=\"curl\")\n",
    "unzip(zipfile=\"./data/activity.zip\",exdir=\"./data\")\n",
    "activity <- read.csv(\"./data/activity.csv\")\n",
    "activity$date <- as.Date(activity$date)\n",
    "activity$interval <- as.factor(activity$interval)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>steps</th><th scope=col>date</th><th scope=col>interval</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>0         </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>5         </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>10        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>15        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>20        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>25        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>30        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>35        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>40        </td></tr>\n",
       "\t<tr><td>NA        </td><td>2012-10-01</td><td>45        </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lll}\n",
       " steps & date & interval\\\\\n",
       "\\hline\n",
       "\t NA         & 2012-10-01 & 0         \\\\\n",
       "\t NA         & 2012-10-01 & 5         \\\\\n",
       "\t NA         & 2012-10-01 & 10        \\\\\n",
       "\t NA         & 2012-10-01 & 15        \\\\\n",
       "\t NA         & 2012-10-01 & 20        \\\\\n",
       "\t NA         & 2012-10-01 & 25        \\\\\n",
       "\t NA         & 2012-10-01 & 30        \\\\\n",
       "\t NA         & 2012-10-01 & 35        \\\\\n",
       "\t NA         & 2012-10-01 & 40        \\\\\n",
       "\t NA         & 2012-10-01 & 45        \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| steps | date | interval |\n",
       "|---|---|---|\n",
       "| NA         | 2012-10-01 | 0          |\n",
       "| NA         | 2012-10-01 | 5          |\n",
       "| NA         | 2012-10-01 | 10         |\n",
       "| NA         | 2012-10-01 | 15         |\n",
       "| NA         | 2012-10-01 | 20         |\n",
       "| NA         | 2012-10-01 | 25         |\n",
       "| NA         | 2012-10-01 | 30         |\n",
       "| NA         | 2012-10-01 | 35         |\n",
       "| NA         | 2012-10-01 | 40         |\n",
       "| NA         | 2012-10-01 | 45         |\n",
       "\n"
      ],
      "text/plain": [
       "   steps date       interval\n",
       "1  NA    2012-10-01 0       \n",
       "2  NA    2012-10-01 5       \n",
       "3  NA    2012-10-01 10      \n",
       "4  NA    2012-10-01 15      \n",
       "5  NA    2012-10-01 20      \n",
       "6  NA    2012-10-01 25      \n",
       "7  NA    2012-10-01 30      \n",
       "8  NA    2012-10-01 35      \n",
       "9  NA    2012-10-01 40      \n",
       "10 NA    2012-10-01 45      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(activity, 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Process the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is mean total number of steps taken per day?\n",
    "1. Calculate the total number of steps taken per day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "steps_per_day <- aggregate(steps ~ date, data=activity, FUN=sum)\n",
    "colnames(steps_per_day) <- c(\"date\", \"steps\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>date</th><th scope=col>steps</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>2012-10-02</td><td>  126     </td></tr>\n",
       "\t<tr><td>2012-10-03</td><td>11352     </td></tr>\n",
       "\t<tr><td>2012-10-04</td><td>12116     </td></tr>\n",
       "\t<tr><td>2012-10-05</td><td>13294     </td></tr>\n",
       "\t<tr><td>2012-10-06</td><td>15420     </td></tr>\n",
       "\t<tr><td>2012-10-07</td><td>11015     </td></tr>\n",
       "\t<tr><td>2012-10-09</td><td>12811     </td></tr>\n",
       "\t<tr><td>2012-10-10</td><td> 9900     </td></tr>\n",
       "\t<tr><td>2012-10-11</td><td>10304     </td></tr>\n",
       "\t<tr><td>2012-10-12</td><td>17382     </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " date & steps\\\\\n",
       "\\hline\n",
       "\t 2012-10-02 &   126     \\\\\n",
       "\t 2012-10-03 & 11352     \\\\\n",
       "\t 2012-10-04 & 12116     \\\\\n",
       "\t 2012-10-05 & 13294     \\\\\n",
       "\t 2012-10-06 & 15420     \\\\\n",
       "\t 2012-10-07 & 11015     \\\\\n",
       "\t 2012-10-09 & 12811     \\\\\n",
       "\t 2012-10-10 &  9900     \\\\\n",
       "\t 2012-10-11 & 10304     \\\\\n",
       "\t 2012-10-12 & 17382     \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| date | steps |\n",
       "|---|---|\n",
       "| 2012-10-02 |   126      |\n",
       "| 2012-10-03 | 11352      |\n",
       "| 2012-10-04 | 12116      |\n",
       "| 2012-10-05 | 13294      |\n",
       "| 2012-10-06 | 15420      |\n",
       "| 2012-10-07 | 11015      |\n",
       "| 2012-10-09 | 12811      |\n",
       "| 2012-10-10 |  9900      |\n",
       "| 2012-10-11 | 10304      |\n",
       "| 2012-10-12 | 17382      |\n",
       "\n"
      ],
      "text/plain": [
       "   date       steps\n",
       "1  2012-10-02   126\n",
       "2  2012-10-03 11352\n",
       "3  2012-10-04 12116\n",
       "4  2012-10-05 13294\n",
       "5  2012-10-06 15420\n",
       "6  2012-10-07 11015\n",
       "7  2012-10-09 12811\n",
       "8  2012-10-10  9900\n",
       "9  2012-10-11 10304\n",
       "10 2012-10-12 17382"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(steps_per_day, 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Make a histogram of the total number of steps taken each day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ggplot(steps_per_day, aes(x = steps)) + \n",
    "  geom_histogram(fill = \"blue\", binwidth = 1000) + \n",
    "  labs(title = \"Histogram - Steps Taken Per Day\", x = \"Steps Per Day\", y = \"Frequency\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Calculate and report the mean and median of the total number of steps taken per day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "10766.1886792453"
      ],
      "text/latex": [
       "10766.1886792453"
      ],
      "text/markdown": [
       "10766.1886792453"
      ],
      "text/plain": [
       "[1] 10766.19"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "10765"
      ],
      "text/latex": [
       "10765"
      ],
      "text/markdown": [
       "10765"
      ],
      "text/plain": [
       "[1] 10765"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mean_steps_per_day <- mean(steps_per_day$steps)\n",
    "mean_steps_per_day\n",
    "median_steps_per_day <- median(steps_per_day$steps)\n",
    "median_steps_per_day"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is the average daily activity pattern?\n",
    "1. Make a time series plot (i.e. type = “l”) of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "steps_per_interval <- aggregate(steps ~ interval, data = activity, FUN = mean, na.rm = TRUE)\n",
    "steps_per_interval$interval <- as.integer(levels(steps_per_interval$interval)[steps_per_interval$interval])\n",
    "colnames(steps_per_interval) <- c(\"interval\", \"steps\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>interval</th><th scope=col>steps</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td> 0       </td><td>1.7169811</td></tr>\n",
       "\t<tr><td> 5       </td><td>0.3396226</td></tr>\n",
       "\t<tr><td>10       </td><td>0.1320755</td></tr>\n",
       "\t<tr><td>15       </td><td>0.1509434</td></tr>\n",
       "\t<tr><td>20       </td><td>0.0754717</td></tr>\n",
       "\t<tr><td>25       </td><td>2.0943396</td></tr>\n",
       "\t<tr><td>30       </td><td>0.5283019</td></tr>\n",
       "\t<tr><td>35       </td><td>0.8679245</td></tr>\n",
       "\t<tr><td>40       </td><td>0.0000000</td></tr>\n",
       "\t<tr><td>45       </td><td>1.4716981</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " interval & steps\\\\\n",
       "\\hline\n",
       "\t  0        & 1.7169811\\\\\n",
       "\t  5        & 0.3396226\\\\\n",
       "\t 10        & 0.1320755\\\\\n",
       "\t 15        & 0.1509434\\\\\n",
       "\t 20        & 0.0754717\\\\\n",
       "\t 25        & 2.0943396\\\\\n",
       "\t 30        & 0.5283019\\\\\n",
       "\t 35        & 0.8679245\\\\\n",
       "\t 40        & 0.0000000\\\\\n",
       "\t 45        & 1.4716981\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| interval | steps |\n",
       "|---|---|\n",
       "|  0        | 1.7169811 |\n",
       "|  5        | 0.3396226 |\n",
       "| 10        | 0.1320755 |\n",
       "| 15        | 0.1509434 |\n",
       "| 20        | 0.0754717 |\n",
       "| 25        | 2.0943396 |\n",
       "| 30        | 0.5283019 |\n",
       "| 35        | 0.8679245 |\n",
       "| 40        | 0.0000000 |\n",
       "| 45        | 1.4716981 |\n",
       "\n"
      ],
      "text/plain": [
       "   interval steps    \n",
       "1   0       1.7169811\n",
       "2   5       0.3396226\n",
       "3  10       0.1320755\n",
       "4  15       0.1509434\n",
       "5  20       0.0754717\n",
       "6  25       2.0943396\n",
       "7  30       0.5283019\n",
       "8  35       0.8679245\n",
       "9  40       0.0000000\n",
       "10 45       1.4716981"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(steps_per_interval, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ggplot(steps_per_interval, aes(x = interval, y = steps)) + \n",
    "  geom_line(col = \"blue\", size = 1) + \n",
    "  labs(title = \"Average Daily Activity Pattern\", x = \"Interval\", y = \"Steps\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Which 5-minute interval, on average across all the days in the dataset, contains the maximum number of steps?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th></th><th scope=col>interval</th><th scope=col>steps</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>104</th><td>835     </td><td>206.1698</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       "  & interval & steps\\\\\n",
       "\\hline\n",
       "\t104 & 835      & 206.1698\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| <!--/--> | interval | steps |\n",
       "|---|---|---|\n",
       "| 104 | 835      | 206.1698 |\n",
       "\n"
      ],
      "text/plain": [
       "    interval steps   \n",
       "104 835      206.1698"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "max_interval <- steps_per_interval[which.max(steps_per_interval$steps),]\n",
    "max_interval"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Imputing missing values\n",
    "1. Calculate and report the total number of missing values in the dataset (i.e. the total number of rows with NAs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "2304"
      ],
      "text/latex": [
       "2304"
      ],
      "text/markdown": [
       "2304"
      ],
      "text/plain": [
       "[1] 2304"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "missing_values <- sum(is.na(activity$steps))\n",
    "missing_values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Devise a strategy for filling in all of the missing values in the dataset. The strategy does not need to be sophisticated. For example, you could use the mean/median for that day, or the mean for that 5-minute interval, etc.\n",
    "\n",
    "\n",
    "To populate missing values, we choose to replace them with the mean value at the same interval across days.\n",
    "\n",
    "3. Create a new dataset that is equal to the original dataset but with the missing data filled in."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_act_data <- activity\n",
    "index_of_na <- which(is.na(new_act_data$steps))\n",
    "for (i in index_of_na) {\n",
    "  new_act_data$steps[i] <- with(steps_per_interval, steps[interval = new_act_data$interval[i]])\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>steps</th><th scope=col>date</th><th scope=col>interval</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1.7169811 </td><td>2012-10-01</td><td>0         </td></tr>\n",
       "\t<tr><td>0.3396226 </td><td>2012-10-01</td><td>5         </td></tr>\n",
       "\t<tr><td>0.1320755 </td><td>2012-10-01</td><td>10        </td></tr>\n",
       "\t<tr><td>0.1509434 </td><td>2012-10-01</td><td>15        </td></tr>\n",
       "\t<tr><td>0.0754717 </td><td>2012-10-01</td><td>20        </td></tr>\n",
       "\t<tr><td>2.0943396 </td><td>2012-10-01</td><td>25        </td></tr>\n",
       "\t<tr><td>0.5283019 </td><td>2012-10-01</td><td>30        </td></tr>\n",
       "\t<tr><td>0.8679245 </td><td>2012-10-01</td><td>35        </td></tr>\n",
       "\t<tr><td>0.0000000 </td><td>2012-10-01</td><td>40        </td></tr>\n",
       "\t<tr><td>1.4716981 </td><td>2012-10-01</td><td>45        </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lll}\n",
       " steps & date & interval\\\\\n",
       "\\hline\n",
       "\t 1.7169811  & 2012-10-01 & 0         \\\\\n",
       "\t 0.3396226  & 2012-10-01 & 5         \\\\\n",
       "\t 0.1320755  & 2012-10-01 & 10        \\\\\n",
       "\t 0.1509434  & 2012-10-01 & 15        \\\\\n",
       "\t 0.0754717  & 2012-10-01 & 20        \\\\\n",
       "\t 2.0943396  & 2012-10-01 & 25        \\\\\n",
       "\t 0.5283019  & 2012-10-01 & 30        \\\\\n",
       "\t 0.8679245  & 2012-10-01 & 35        \\\\\n",
       "\t 0.0000000  & 2012-10-01 & 40        \\\\\n",
       "\t 1.4716981  & 2012-10-01 & 45        \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| steps | date | interval |\n",
       "|---|---|---|\n",
       "| 1.7169811  | 2012-10-01 | 0          |\n",
       "| 0.3396226  | 2012-10-01 | 5          |\n",
       "| 0.1320755  | 2012-10-01 | 10         |\n",
       "| 0.1509434  | 2012-10-01 | 15         |\n",
       "| 0.0754717  | 2012-10-01 | 20         |\n",
       "| 2.0943396  | 2012-10-01 | 25         |\n",
       "| 0.5283019  | 2012-10-01 | 30         |\n",
       "| 0.8679245  | 2012-10-01 | 35         |\n",
       "| 0.0000000  | 2012-10-01 | 40         |\n",
       "| 1.4716981  | 2012-10-01 | 45         |\n",
       "\n"
      ],
      "text/plain": [
       "   steps     date       interval\n",
       "1  1.7169811 2012-10-01 0       \n",
       "2  0.3396226 2012-10-01 5       \n",
       "3  0.1320755 2012-10-01 10      \n",
       "4  0.1509434 2012-10-01 15      \n",
       "5  0.0754717 2012-10-01 20      \n",
       "6  2.0943396 2012-10-01 25      \n",
       "7  0.5283019 2012-10-01 30      \n",
       "8  0.8679245 2012-10-01 35      \n",
       "9  0.0000000 2012-10-01 40      \n",
       "10 1.4716981 2012-10-01 45      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(new_act_data, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "0"
      ],
      "text/latex": [
       "0"
      ],
      "text/markdown": [
       "0"
      ],
      "text/plain": [
       "[1] 0"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "new_missing_values <- sum(is.na(new_act_data$steps))\n",
    "new_missing_values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Make a histogram of the total number of steps taken each day and Calculate and report the mean and median total number of steps taken per day. Do these values differ from the estimates from the first part of the assignment? What is the impact of imputing missing data on the estimates of the total daily number of steps?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n/f/X7ppv116ovV23u/t8t/W2en3c4Ks5Z32cr/J2J0hzpPdWLpI3iLR49qdzze79fFugFeBf\nc5G3a6w5qXE4dtd8++NndbkVcfbkdCp6fdx6d3zYoHuwqd4bpaqzVidxP2ccXSlBpOVz+Ldp\nzinN8m4F2LRNqV7ai7WTaM3ppq5e7+4bXO8l7B+33t82eHiw//i3bR69NLxK4d9arS6IJJGv\n3eu2OW+06/5iyUWD5uPH6QJuc+dJe5uvvf39vPXxssvtwfayxdfJt4/L5R/JGUSSSXOmGBTp\nJMGmqi/XZPc3934U6bM5U71Wm7ePfXey2++4JT5FEGnxVNWh+/xwaXf+0r65tOtuxb09XbCd\nc7/18fnhy/m50/F8U7C577CrafkUYVYXz67ans40h935aU77hV1zb23b3mw4HrbNXba6+jxd\nmD3ebLjsftv6+sXb60jt/3w2lPZLm2rwtScSCSItn033lGffrPnTyj/Ul3ctNDe02y91t78v\n963vRbrf+vrF692Iz+u+5+9+VM1TMZI9iCSQt23zgmlzgffWWnM6k7RnqebSblu9tvcYTpdk\n9fX1n4c3QNxtfbxt0L64tDtfNLYbdN+9u7VHMgaRlDPyHUO/yCdva5gmiKSc/CJtuWc3TRBJ\nOblFqrjVMFUQSTm5RaqbO4NkiiASIRmCSIRkCCIRkiGIREiGIBIhGYJIhGQIIhGSIYhESIb8\nP5XqitbjKFzEAAAAAElFTkSuQmCC",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "new_steps_per_day <- aggregate(steps ~ date, data = new_act_data, FUN=sum)\n",
    "colnames(new_steps_per_day) <- c(\"date\", \"steps\")\n",
    "ggplot(new_steps_per_day, aes(x = steps)) + \n",
    "  geom_histogram(fill = \"blue\", binwidth = 1000) + \n",
    "  labs(title = \"Histogram - Steps Taken Per Day\", x = \"Steps Per Day\", y = \"Frequency\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "10766.1886792453"
      ],
      "text/latex": [
       "10766.1886792453"
      ],
      "text/markdown": [
       "10766.1886792453"
      ],
      "text/plain": [
       "[1] 10766.19"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "10766.1886792453"
      ],
      "text/latex": [
       "10766.1886792453"
      ],
      "text/markdown": [
       "10766.1886792453"
      ],
      "text/plain": [
       "[1] 10766.19"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "new_mean_steps_per_day <- mean(new_steps_per_day$steps)\n",
    "new_mean_steps_per_day\n",
    "new_median_steps_per_day <- median(new_steps_per_day$steps)\n",
    "new_median_steps_per_day"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Are there differences in activity patterns between weekdays and weekends?\n",
    "\n",
    "1. Create a new factor variable in the dataset with two levels - “weekday” and “weekend” indicating whether a given date is a weekday or weekend day.\n",
    "\n",
    "Let us first add a factor variable to identify the given date as Weekday or Weekend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>steps</th><th scope=col>date</th><th scope=col>interval</th><th scope=col>weekday</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1.7169811 </td><td>2012-10-01</td><td> 0        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.3396226 </td><td>2012-10-01</td><td> 5        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.1320755 </td><td>2012-10-01</td><td>10        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.1509434 </td><td>2012-10-01</td><td>15        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.0754717 </td><td>2012-10-01</td><td>20        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>2.0943396 </td><td>2012-10-01</td><td>25        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.5283019 </td><td>2012-10-01</td><td>30        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.8679245 </td><td>2012-10-01</td><td>35        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>0.0000000 </td><td>2012-10-01</td><td>40        </td><td>Weekday   </td></tr>\n",
       "\t<tr><td>1.4716981 </td><td>2012-10-01</td><td>45        </td><td>Weekday   </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|llll}\n",
       " steps & date & interval & weekday\\\\\n",
       "\\hline\n",
       "\t 1.7169811  & 2012-10-01 &  0         & Weekday   \\\\\n",
       "\t 0.3396226  & 2012-10-01 &  5         & Weekday   \\\\\n",
       "\t 0.1320755  & 2012-10-01 & 10         & Weekday   \\\\\n",
       "\t 0.1509434  & 2012-10-01 & 15         & Weekday   \\\\\n",
       "\t 0.0754717  & 2012-10-01 & 20         & Weekday   \\\\\n",
       "\t 2.0943396  & 2012-10-01 & 25         & Weekday   \\\\\n",
       "\t 0.5283019  & 2012-10-01 & 30         & Weekday   \\\\\n",
       "\t 0.8679245  & 2012-10-01 & 35         & Weekday   \\\\\n",
       "\t 0.0000000  & 2012-10-01 & 40         & Weekday   \\\\\n",
       "\t 1.4716981  & 2012-10-01 & 45         & Weekday   \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| steps | date | interval | weekday |\n",
       "|---|---|---|---|\n",
       "| 1.7169811  | 2012-10-01 |  0         | Weekday    |\n",
       "| 0.3396226  | 2012-10-01 |  5         | Weekday    |\n",
       "| 0.1320755  | 2012-10-01 | 10         | Weekday    |\n",
       "| 0.1509434  | 2012-10-01 | 15         | Weekday    |\n",
       "| 0.0754717  | 2012-10-01 | 20         | Weekday    |\n",
       "| 2.0943396  | 2012-10-01 | 25         | Weekday    |\n",
       "| 0.5283019  | 2012-10-01 | 30         | Weekday    |\n",
       "| 0.8679245  | 2012-10-01 | 35         | Weekday    |\n",
       "| 0.0000000  | 2012-10-01 | 40         | Weekday    |\n",
       "| 1.4716981  | 2012-10-01 | 45         | Weekday    |\n",
       "\n"
      ],
      "text/plain": [
       "   steps     date       interval weekday\n",
       "1  1.7169811 2012-10-01  0       Weekday\n",
       "2  0.3396226 2012-10-01  5       Weekday\n",
       "3  0.1320755 2012-10-01 10       Weekday\n",
       "4  0.1509434 2012-10-01 15       Weekday\n",
       "5  0.0754717 2012-10-01 20       Weekday\n",
       "6  2.0943396 2012-10-01 25       Weekday\n",
       "7  0.5283019 2012-10-01 30       Weekday\n",
       "8  0.8679245 2012-10-01 35       Weekday\n",
       "9  0.0000000 2012-10-01 40       Weekday\n",
       "10 1.4716981 2012-10-01 45       Weekday"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dt <- data.table(new_act_data)\n",
    "dt[, weekday := ifelse(weekdays(date) %in% c(\"Saturday\", \"Sunday\"), \"Weekend\", \"Weekday\")]\n",
    "dt$weekday <- as.factor(dt$weekday)\n",
    "dt$interval <- as.integer(levels(dt$interval)[dt$interval])\n",
    "head(dt, 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Make a panel plot containing a time series plot (i.e. type = “l”) of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekday days or weekend days (y-axis)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAMAAADKOT/pAAAAPFBMVEUAAAAAAP8aGhozMzNN\nTU1oaGh8fHyMjIyampqnp6eysrK9vb3Hx8fQ0NDZ2dnh4eHp6enr6+vw8PD///+LxCthAAAA\nCXBIWXMAABJ0AAASdAHeZh94AAAgAElEQVR4nO2diZabvBIGzcQz2f47CfH7v+sdL4AkJCGB\n1DSivnMS2yxFAyoLMGNfboSQzbnsXQAhLQSRCCkQRCKkQBCJkAJBJEIKBJEIKRBEIqRAEImQ\nAtks0ichpw0iEVIgiERIgSASIQWCSIQUCCIRUiCIREiBIBIhBYJIhBQIIhFSIIhESIEg0mHy\n5nuYjw+MJXWDSIfJ2+v/N+PVfPz8OZEIIh0nb8//3sbnntGe50QiiHScuCK9feVzehyG319N\no0P9FykbRDpO3ux/ozjG4/DwZmuHSNWDSMfJskhmx/RpjMaj6kGkA8Xtdl4Hb8Oj4ZBxyIdI\nIkGkA2U6UDPtGB/f7B5p+odH9YNIB8qCSJ/eIz5EEgkiHSmWOwkXG94QSSqIdKTYndDy5e/g\nZ06kdBCp/SCSQBCp/SCSQBCp9bzhkUQQiZACQSRCCgSRCCkQRCKkQBCJkAJBJEIKpKBI/XJS\npkkLJGGSwpJUkRAJkiyoURIiQZIFNUpCJEiyoEZJiARJFtQoCZEgyYIaJSESJFlQoyREgiQL\napSESJBkQY2SEAmSLKhREiJBkgU1SkIkSLKgRkmIBEkW1CgJkSDJgholIRIkWVCjJEQSIHXF\nSNlBJCESItUndV2uSQrXTmFJqkiIhEiyoEZJiIRIsqBGSYiESLKgRkmIhEiyoEZJiIRIsqBG\nSYiESLKgRkkFRSKBfIm0dwlELvRItUj0SCcgIZKISJkmKVw7hSWpIiESIsmCGiUhUnVSh0gn\nICESIsmCGiUhEiLJgholIRIiyYIaJSESIsmCGiUhEiLJgholIRIiyYIaJSESIsmCGiUhEiLJ\ngholIRIiyYIaJSESIsmCGiUhEiLJgholIRIiyYIaJSESIsmCGiUhEiLJgholIRIiyYIaJSES\nIsmCGiUhkoxIeSYpXDuFJakiIRIiyYIaJSESIsmCGiUhEiLJgholIRIiyYIaJSFSbdJdIkRq\nnoRIiCQLapSESIgkC2qUhEiIJAtqlIRIiCQLapSUJdL1K75HRIqQEOkUpByRrq//3EdEipEQ\n6RQkRKpL6hDpHKQckQabECmZ9PowFpGaJ5UR6ds9afOfK0+R+PHLMyVNpOuNHimDRI90FhIi\nIZIsqFFSpkhX8z9EWiQh0llIeSJdLZsQaZGESGchZYl0tbslRFokIdJZSDkiXa+vWxm4syGV\nhEhnIWX1SPGI1HswEiKdhYRIiCQLapSESBIi5ZqkcO0UlqSKhEiIJAtqlIRIiCQLapSESDVJ\nnSFSjkkK105hSapIiFRfpB6R2ichEiLJgholIRIiyYIaJSESIsmCGiUhEiLJgholIZKYSBkm\nKVw7hSWpIiESIsmCGiUhEiLJgholIZKISJknSQrXTmFJqkiIJCNS3k1CCtdOYUmqSIiESLKg\nRkmIVFmkvpuebiCtDSIJkRCptkjzp2tIa4NIQiREQiRZUKMkREIkWVCjJEQSEinLJIVrp7Ak\nVSREQiRZUKMkREIkWVCjJERCJFlQoyREQiRZUKMkRBIUKdkkhWunsCRVJESSEinHJIVrp7Ak\nVaSCIpFZOusnL7uOX8A8QeiRypOcPii5T1K4dgpLUkVCJEGRkk1SuHYKS1JFQiRJkVJNUrh2\nCktSRUKkiiSPNWkmKVw7hSWpIiGSrEhpJilcO4UlqSIhkrBISSYpXDuFJakiIZK0SCkmKVw7\nhSWpIiGSuEgJJilcO4UlqSIhkrxIyyYpXDuFJakiIdIOIi2apHDtFJakioRIe4i0dCu4wrVT\nWJIqEiIhkiyoURIiIZIsqFESIiGSLKhREiIhkiyoURIiIZIsqFESIiGSLKhREiIhkiyoURIi\nIZIsqFESIiGSLKhREiIhkiyoURIiIZIsqFESIiGSLKhREiIhkiyoURIiIZIsqFESIiGSLKhR\nEiIhkiyoURIiIZIsqFESIiGSLKhRUqZI1+f/97weESlIitiCSK2R8kR6eXM1rJpMEqn3SCRE\nOhEpS6TrDZEySIh0IlJej2S7g0hxEiKdiLRKpOEUaRzy7Z6U+U+VyA/08dt97SazR7rSIy2R\n6JFORFoj0vAMkeIkRDoRCZEQSRbUKGmNSBzapZEQ6USktSLZFxsQyUdCpBOR1og03tHAnQ1R\nUsyWuEkK105hSapImSLFIlLvkUiIdCISIiGSLKhREiIhkiyoURIiIZIsqFESIiGSLKhREiIh\nkiyoURIiIZIsqFESIiGSLKhREiIhkiyoURIiIZIsqFESIiGSLKhREiIhkiyoURIiIZIsqFES\n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\nQmCC",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "steps_per_weekday <- aggregate(steps ~ interval+weekday, data = dt, FUN = mean)\n",
    "ggplot(steps_per_weekday, aes(x = interval, y = steps)) + \n",
    "  geom_line(col = \"blue\", size = 1) + \n",
    "  facet_wrap(~ weekday, nrow=2, ncol=1) + \n",
    "  labs(x = \"Interval\", y = \"Number of Steps\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Looking at the above graph we notice that the activity on weekdays has the highest peak (> 300) compared to all intervals and only one other peak that touches 100. On the contrary, weekend intervals have more peaks over a hundred than weekday. May be the person from whomever the data is collected is engaged in more active life style during weekends compared to weekdays."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R 4.0.0",
   "language": "R",
   "name": "ir35"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
