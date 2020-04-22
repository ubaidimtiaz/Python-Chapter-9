with Temp as
         (
             select split_part(cat_petting.pet_detection.names, ' ', 1) as firstname,
                    split_part(cat_petting.pet_detection.names, ' ', 2) as lastname,
                    cat_petting.pet_detection.petting_start as pstart,
                    cat_petting.pet_detection.petting_end as pend



             from cat_petting.pet_detection
         )
select * from Temp
where firstname like 'D%' and lastname like 'B%'


