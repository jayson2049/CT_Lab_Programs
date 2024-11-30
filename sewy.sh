awk'/^(ATOM)/ {
  x+=$7;y+=$8;z+=$9; total_mass+=1;
}
END

