#printf "2N8bXfrWTzqZoV89dosge2JxvE38VnHurqD" | base58 -dc | xxd -p | cut -c 2-
printf "2N8bXfrWTzqZoV89dosge2JxvE38VnHurqD" | bx base58check-decode

#pay to [a9 14 20byte-hash 87]
