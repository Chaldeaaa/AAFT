library(dplyr)

setwd('/content/drive/MyDrive/AAFT_Draft/Data')

# data of user profiles
profiles <- read.csv("profiles.csv")

# names(profiles)
head(profiles)

# make stuff english
colnames(profiles) <- c("ID", "gender", "age", "income", "marr", "job", "loc", "marExp", "parExp", "marType", "child", "childExp", "cert", "cores", "jobType", "locPref", "ssPar", "ssParExp", "out", "edu")

# gender modif
profiles$gender[profiles$gender == '男'] <- "Male"
profiles$gender[profiles$gender == '女'] <- "Female"

# age cleaning
profiles$age <- gsub("岁", "", profiles$age)
profiles$age <- as.numeric(profiles$age)

# marr status
profiles$marr <- gsub("丧偶", "Widowed", profiles$marr)
profiles$marr <- gsub("未婚", "Single", profiles$marr)
profiles$marr <- gsub("离异", "Divorced", profiles$marr)

# unique(profiles$income)
profiles$income <- gsub("5万以下","< 50k", profiles$income)
profiles$income <- gsub("5-10万","50 to 100k", profiles$income)
profiles$income <- gsub("10-20万","100 to 200k", profiles$income)
profiles$income <- gsub("20-30万","200 to 300k", profiles$income)
profiles$income <- gsub("30-50万","300 to 500k", profiles$income)
profiles$income <- gsub("50-100万","500 to 1000k", profiles$income)
profiles$income <- gsub("100万以上","< 1000k", profiles$income)

profiles$income <- factor(profiles$income, levels = c("< 50k", "50 to 100k", "100 to 200k", "200 to 300k", "300 to 500k", "500 to 1000k", "< 1000k"))

# unique(profiles$job)
profiles$job <- profiles$job %>%
  gsub("普通员工", "Ordinary Employee", .) %>%
  gsub("技术员", "Technician", .) %>%
  gsub("公务员", "Civil Servant", .) %>%
  gsub("教师", "Teacher", .) %>%
  gsub("中层管理", "Middle Management", .) %>%
  gsub("自由职业", "Freelancer", .) %>%
  gsub("医生", "Doctor", .) %>%
  gsub("设计师", "Designer", .) %>%
  gsub("工程师", "Engineer", .) %>%
  gsub("个体老板", "Self-employed", .) %>%
  gsub("护士", "Nurse", .) %>%
  gsub("运动员", "Athlete", .) %>%
  gsub("模特", "Model", .) %>%
  gsub("教授", "Professor", .) %>%
  gsub("副总/总监", "Vice President/Director", .) %>%
  gsub("部门经理", "Department Manager", .) %>%
  gsub("学生", "Student", .) %>%
  gsub("艺术家", "Artist", .) %>%
  gsub("律师", "Lawyer", .) %>%
  gsub("总经理", "General Manager", .) %>%
  gsub("专家学者", "Expert/Scholar", .) %>%
  gsub("董事长", "Chairman", .) %>%
  gsub("企业家", "Entrepreneur", .) %>%
  gsub("无业", "Unemployed", .) %>%
  gsub("高级干部", "Senior Cadre", .) %>%
  gsub("服务员", "Waiter/Waitress", .) %>%
  gsub("离/退休", "Retired", .) %>%
  gsub("演员", "Actor", .)

# output
write.csv(profiles, "profilesCleaned.csv", row.names = FALSE)

