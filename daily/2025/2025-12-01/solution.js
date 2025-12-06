/*
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2025-12-01                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
*/

function convertToKm(miles) {
  let wynik = 1.60934 * parseFloat(miles);
  return Math.round(wynik * 100) / 100;
}

console.log(
convertToKm(1))