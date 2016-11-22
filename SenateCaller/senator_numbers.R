library(XML)

senators <- xmlParse(file = "http://www.senate.gov/general/contact_information/senators_cfm.xml")

the_list <- xmlToList(senators)

phones <- sapply(the_list, function(x) x['phone'])

phone_nums <- as.character(phones)
phones_no_punct <- gsub("\\(|\\)|-| ", "", phone_nums)

phones_no_punct <- phones_no_punct[-which(is.na(phones_no_punct))]

final_phones <- paste0("+1", phones_no_punct)

write.csv(file="~/Documents/Twilio/senator_phones.csv", final_phones, row.names = FALSE)
