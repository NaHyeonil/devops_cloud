import { useState } from "react";

function reducer(action, prevState) {
  const { type, amount } = action;
  if (type === "PLUS") {
    return prevState + amount;
  } else if (type === "MINUS") {
    return prevState - amount;
  }
  return prevState;
}

function reducer_color(action, prevState_color) {
  const { type, color } = action;
  if (type === "CHANGE_COLOR") {
    return color;
  }
  return prevState_color;
}

function Counter1() {
  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const handlePlus = () => {
    const action = { type: "PLUS", amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const handleMinus = () => {
    const action = { type: "MINUS", amount: 1 };
    setValue((prevValue) => {
      return reducer(action, prevValue);
    });
  };

  const greenBotton = () => {
    const action = { type: "CHANGE_COLOR", color: "green" };
    setColor(() => {
      return reducer_color(action, color);
    });
  };
  const blueBotton = () => {
    const action = { type: "CHANGE_COLOR", color: "blue" };
    setColor(() => {
      return reducer_color(action, color);
    });
  };
  const redBotton = () => {
    const action = { type: "CHANGE_COLOR", color: "red" };
    setColor(() => {
      return reducer_color(action, color);
    });
  };

  // 1-6
  //   const { value, color } = state;
  //   const newPlusState = () => {
  //     setState((prevState) => ({ ...prevState, value: prevState.value + 1 }));
  //   };
  //   const newMinusState = () => {
  //     setState((prevState) => ({ ...prevState, value: prevState.value - 1 }));
  //   };
  //   const newGBottonState = () => {
  //     setState((prevState) => ({ ...prevState, color: "green" }));
  //   };
  //   const newBBottonState = () => {
  //     setState((prevState) => ({ ...prevState, color: "blue" }));
  //   };
  //   const newRBottonState = () => {
  //     setState((prevState) => ({ ...prevState, color: "red" }));
  //   };

  //   const [value, setValue] = useState(0);
  //   const [color, setColor] = useState("red");
  //   //   const handlePlus = () => {
  //   //     setValue(value + 1);
  //   //   };
  //   //   const handleMinus = () => {
  //   //     setValue(value - 1);
  //   //   };
  //   const handlePlus = () => {
  //     setValue((prevValue) => prevValue + 1);
  //   };
  //   const handleMinus = () => {
  //     setValue((prevValue) => prevValue - 1);
  //   };

  //   //   const greenBotton = () => {
  //   //     setColor("green");
  //   //   };
  //   //   const blueBotton = () => {
  //   //     setColor("blue");
  //   //   };
  //   //   const redBotton = () => {
  //   //     setColor("red");
  //   //   };
  //   const greenBotton = () => {
  //     setColor(() => "green");
  //   };

  //   const blueBotton = () => {
  //     setColor(() => "blue");
  //   };

  //   const redBotton = () => {
  //     setColor(() => "red");
  //   };

  return (
    <div>
      <h2>Counter</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
      <button onClick={greenBotton}>green</button>
      <button onClick={blueBotton}>blue</button>
      <button onClick={redBotton}>red</button>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter1;
