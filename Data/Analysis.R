require(ggplot2)
require(dplyr)
require(tidyverse)
require(RColorBrewer)

# getwd()
setwd("/content/drive/MyDrive/AAFT_Draft/Data")

source("Cleaning.R")

dim(profiles)
head(profiles)

# unique(profiles$marr)
profiles$marr <- factor(profiles$marr, levels = c("Single", "Divorced", "Widowed"))

ggplot(profiles %>% filter(!is.na(marr)), aes(x = marr, fill = marr)) +
  geom_bar() +
  scale_fill_brewer(palette = "Pastel1") +
  labs(y = "User", title = "Marriage Status Distribution", fill = "Status") +
  theme_bw()

ggplot(profiles %>% filter(!is.na(gender)), aes(x = gender, fill = gender)) +
  geom_bar() +
  scale_fill_brewer(palette = "Pastel1") +
  labs(x = "Gender", y = "User", title = "Gender Distribution", fill = "Gender") +
  theme_bw()

ggplot(profiles %>% filter(!is.na(income)), aes(x = income, fill = gender)) +
  geom_bar() +
  scale_fill_brewer(palette = "Pastel1") +
  labs(x = "Income Level", y = "User", title = "Income Level Distribution by Gender", fill = "Gender") +
  theme_bw()

ggplot(profiles %>% filter(!is.na(age)), aes(x = age, fill = gender)) +
  geom_density(alpha = 0.4) +
  scale_fill_brewer(palette = "Pastel1") +
  labs(title = "Age Distribution by Gender", x = "Age", y = "Density", fill = "Gender") +
  theme_bw()

ggplot(profiles %>% filter(!is.na(job)), aes(x = job, fill = gender)) +
  geom_bar() +
  scale_fill_brewer(palette = "Pastel1") +
  labs(x = "Occupation", y = "User", title = "Occupation Distribution by Gender", fill = "Gender") +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))

ggplot(profiles %>% filter(gender == "Female", !is.na(job)), aes(x = job)) +
  geom_bar(fill = "salmon") +
  scale_fill_brewer(palette = "Pastel1") +
  labs(x = "Occupation", y = "User", title = "Female Occupation Distribution") +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))

