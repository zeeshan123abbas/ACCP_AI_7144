import { Component } from "react";

export default class ClassCounter extends Component {
  state = { count: 0 };

  increment = () => {
    this.setState((prev) => ({ count: prev.count + 1 }));
  };

  render() {
    return (
      <button onClick={this.increment}>
        Clicked {this.state.count} times ({this.props.label})
      </button>
    );
  }
}
