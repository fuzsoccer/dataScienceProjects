a <- read.csv('data/raw/study_2_analysis_data_deid.csv')
a$risk_messages <- as.integer(a$algo_condition %in% c('unspecified','medrec','algorithm'))
a$reasons <- as.integer(a$algo_condition %in% c('medrec','algorithm'))
a$contactcontrol <- as.integer(a$algo_condition == 'control')
models <- list(
  lm(vaccinated ~ risk_messages, data=a, subset=algo_condition != 'nocontact'),
  lm(vaccinated ~ risk_messages, data=a, subset=algo_condition != 'control'),
  lm(vaccinated ~ reasons, data=a, subset=!algo_condition %in% c('nocontact','control')),
  lm(vaccinated ~ contactcontrol, data=a, subset=algo_condition %in% c('nocontact','control'))
)
checks <- do.call(rbind,lapply(models,function(m) coef(summary(m))[2,c(1,2,4)]))
write.csv(checks,'validation/r_model_validation.csv',row.names=FALSE)
