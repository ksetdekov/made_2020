
gdis<-ada(Y~.,data=training[,-c(10)],iter=1000,nu=1,type="discrete")
gdis=addtest(gdis,testing[,-31],testing[,31])
plot(gdis,TRUE,TRUE)
varplot(gdis)
pairs(gdis,testing[,-31],maxvar=2)
adares <- predict(gdis, newdata =  test)
adares_prob <- predict(gdis, newdata =  test ,type="prob")
export <- adares_prob[,2]

MLmetrics::Accuracy(adares,testing$Y)

