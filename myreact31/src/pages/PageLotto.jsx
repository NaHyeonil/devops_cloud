import { useState } from 'react';

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

function PageLotto() {
  const [numbers, setNumber] = useState([10, 11, 12, 13, 14, 15, 16]);
  const handleClick = () => setNumber(makeLottoNumbers());

  return (
    <>
      <h2>Lotto</h2>
      <div>
        {numbers.map((numbers) => {
          return (
            <div
              style={{
                backgroundColor: 'lightgrey',
                width: '50px',
                height: '50px',
                borderRadius: '25px',
                lineHeight: '45px',
                textAlign: 'center',
                display: 'inline-block',
                fontSize: '2rem',
                margin: '0.5rem',
                userSelect: 'none',
              }}
            >
              {numbers}

            </div>
          );
        })}
        <button onClick={handleClick}>예지</button>
      </div>
    </>
  );
}

export default PageLotto;
