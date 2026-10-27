# Run from the project root; explicit references align with Python coding.
a <- read.csv('data/raw/study_2_analysis_data_deid.csv')
d <- subset(a, algo_condition %in% c('medrec','algorithm'))
d$algo_condition <- factor(d$algo_condition, levels=c('medrec','algorithm'))
d$num_reasons <- factor(d$num_reasons, levels=c('1reason','3reasons'))
m <- lm(vaccinated ~ algo_condition * num_reasons, data=d)
s <- coef(summary(m))
write.csv(data.frame(term=rownames(s), estimate=s[,1], standard_error=s[,2], p_value=s[,4]),
          'validation/r_reasons_validation.csv',row.names=FALSE)
