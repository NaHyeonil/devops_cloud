import { useState } from 'react';
import Circle from './Circle';

const INITIAL_STATE = {
  numbers: [0, 0, 0, 0, 0, 0, 0],
  colors: [
    '#1B62BF',
    '#1755A6',
    '#37A647',
    '#F29F05',
    '#F23838',
    'purple',
    'pink',
  ],
};

const zip = (...rows) =>
  [...rows[0]].map((_, column_index) => rows.map((row) => row[column_index]));

const makeLottoNumbers = () => {
  const lottoSet = new Set();
  while (lottoSet.size < 7) {
    let randomNum = Math.floor(Math.random() * 45) + 1;
    lottoSet.add(randomNum);
  }
  const lottoList = Array.from(lottoSet);
  lottoList.sort((a, b) => a - b);
  return lottoList;
};

const shuffle_array = (array) =>
  array.sort(() => Math.random() - Math.random());

function SevenNumbers() {
  const [state, setState] = useState(INITIAL_STATE);

  const randomNumbers = () => {
    setState((prevState) => ({
      ...prevState,
      numbers: makeLottoNumbers(),
    }));
  };
  const shuffleNumbers = () => {
    setState((prevState) => ({
      ...prevState,
      numbers: shuffle_array(prevState.numbers),
    }));
  };
  const shuffleColors = () => {
    setState((prevState) => ({
      ...prevState,
      colors: shuffle_array(prevState.colors),
    }));
  };

  return (
    <div>
      <h2>7개의 숫자</h2>
      {zip(state.numbers, state.colors).map(([number, color]) => (
        <Circle number={number} backgroundColor={color} />
      ))}
      <hr />
      <button onClick={randomNumbers}>로또번호</button>
      <button onClick={shuffleNumbers}>번호섞기</button>
      <button onClick={shuffleColors}>색깔섞기</button>
    </div>
  );
}

export default SevenNumbers;
